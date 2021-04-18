from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from DeviceAPI.models import (
    Dose,
    Chamber,
    Treatment,
    Medicine,
    Device,
    DeviceVersion,
    Container,
    ContainerVersion,
)
from uuid import UUID
from collections import OrderedDict


class DoseViewTestCase(APITestCase):
    doses_url = "/api/doses/"

    def setUp(self):
        self.owner = get_user_model().objects.create(
            email="testemail@test.com",
            password="testpassword"
        )
        tokens = RefreshToken.for_user(self.owner)
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + str(tokens.access_token)
        )
        self.device_version = DeviceVersion.objects.create(
            name="0.0",
            capacity=3,
            latest_firmware_version="0.0.0"
        )
        self.device = Device.objects.create(
            owner=self.owner,
            version=self.device_version,
            name="TestBox"
        )
        self.container_version = ContainerVersion.objects.create(
            name="0.1",
            capacity=20
        )
        self.container = Container.objects.create_with_chambers(
            version=self.container_version,
            device=self.device,
            position=0
        )
        self.treatment = Treatment.objects.create(
            associated_user=self.owner,
            name="John's treatment",
            beneficiary="John",
        )
        self.medicine = Medicine.objects.create(
            name="testname",
            producer="testproducer"
        )
        self.additional_device = Device.objects.create(
            owner=self.owner,
            version=self.device_version,
            name="AdditionalTestBox"
        )
        self.additional_container = Container.objects.create_with_chambers(
            version=self.container_version,
            device=self.additional_device,
            position=0
        )
        self.additional_medicine = Medicine.objects.create(
            name="Additional_testname",
            producer="Additional_testproducer"
        )
        self.doses = []
        for i in range(3):
            self.doses.append(
                Dose.objects.create(
                    treatment=self.treatment,
                    chamber=Chamber.objects.filter(container=self.container.uuid).first(),
                    medicine=self.medicine,
                    planned_administration_time="2021-04-18T12:12:10.612000Z",
                    number_of_pills=2.0,
                    on_demand=True
                )
            )
        self.additional_doses = []
        for i in range(2):
            self.additional_doses.append(
                Dose.objects.create(
                    treatment=self.treatment,
                    chamber=Chamber.objects.filter(container=self.additional_container.uuid).first(),
                    medicine=self.additional_medicine,
                    planned_administration_time="2021-04-20T12:12:10.612000Z",
                    number_of_pills=2.0,
                    on_demand=True
                )
            )

    def test_dose_list_all(self):
        expected_data = []

        for i in range(3):
            expected_data.append(
                OrderedDict(
                    uuid=str(self.doses[i].uuid),
                    treatment=UUID(str(self.doses[i].treatment.uuid)),
                    chamber=UUID(str(self.doses[i].chamber.uuid)),
                    medicine=UUID(str(self.doses[i].medicine.uuid)),
                    planned_administration_time=self.doses[i].planned_administration_time,
                    number_of_pills=self.doses[i].number_of_pills,
                    on_demand=self.doses[i].on_demand,
                )
            )
        for i in range(2):
            expected_data.append(
                OrderedDict(
                    uuid=str(self.additional_doses[i].uuid),
                    treatment=UUID(str(self.additional_doses[i].treatment.uuid)),
                    chamber=UUID(str(self.additional_doses[i].chamber.uuid)),
                    medicine=UUID(str(self.additional_doses[i].medicine.uuid)),
                    planned_administration_time=self.additional_doses[i].planned_administration_time,
                    number_of_pills=self.additional_doses[i].number_of_pills,
                    on_demand=self.additional_doses[i].on_demand,
                )
            )
        response = self.client.get(self.doses_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data, expected_data)

    def test_dose_retrieve(self):
        expected_data = {
            "uuid": str(self.doses[0].uuid),
            "treatment": UUID(str(self.doses[0].treatment.uuid)),
            "chamber": UUID(str(self.doses[0].chamber.uuid)),
            "medicine": UUID(str(self.doses[0].medicine.uuid)),
            "planned_administration_time": self.doses[0].planned_administration_time,
            "number_of_pills": self.doses[0].number_of_pills,
            "on_demand": self.doses[0].on_demand,
        }
        response = self.client.get(
            self.doses_url + f"{self.doses[0].uuid}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_dose_create(self):
        input_data = {
            "treatment": self.treatment.uuid,
            "chamber": self.additional_doses[0].chamber.uuid,
            "medicine": self.medicine.uuid,
            "planned_administration_time": "2021-04-18T12:12:10.612000Z",
            "number_of_pills": 3.0,
            "on_demand": True,
        }
        response = self.client.post(
            self.doses_url,
            input_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_dose_update(self):
        expected_data = OrderedDict(
            uuid=str(self.doses[0].uuid),
            treatment=UUID(str(self.treatment.uuid)),
            chamber=Chamber.objects.filter(container=self.container.uuid).first().uuid,
            medicine=self.medicine.uuid,
            planned_administration_time="2021-04-18T12:12:10.612000Z",
            number_of_pills=2.0,
            on_demand=True
        )
        input_data = OrderedDict(
            treatment=UUID(str(self.treatment.uuid)),
            chamber=Chamber.objects.filter(container=self.container.uuid).first().uuid,
            medicine=self.medicine.uuid,
            planned_administration_time="2021-04-18T12:12:10.612000Z",
            number_of_pills=2.0,
            on_demand=True
        )

        response = self.client.put(
            self.doses_url + f"{self.doses[0].uuid}",
            input_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_dose_destroy(self):

        response = self.client.delete(
            self.doses_url + f"{self.doses[0].uuid}"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
