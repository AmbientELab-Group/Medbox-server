from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from DeviceAPI.models import (
    Chamber,
    Container,
    ContainerVersion,
    Device,
    DeviceVersion
)
from collections import OrderedDict


class ChamberListTestCase(APITestCase):
    chambers_url = "/api/chambers"

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
            position=1
        )
        self.additional_device = Device.objects.create(
            owner=self.owner,
            version=self.device_version,
            name="TestBox2"
        )
        self.additional_container = Container.objects.create_with_chambers(
            version=self.container_version,
            device=self.additional_device,
            position=1
        )

    def test_chamber_list_all(self):
        expected_data = []
        chambers = Chamber.objects.filter(container=self.container.uuid)
        for pos in range(chambers.count()):
            expected_data.append(
                OrderedDict(
                    uuid=str(chambers[pos].uuid),
                    position=chambers[pos].position,
                    is_full=chambers[pos].is_full,
                    real_administration_time=chambers[pos].real_administration_time
                )
            )
        additional_chambers = Chamber.objects.filter(container=self.additional_container.uuid)
        for pos in range(additional_chambers.count()):
            expected_data.append(
                OrderedDict(
                    uuid=str(additional_chambers[pos].uuid),
                    position=additional_chambers[pos].position,
                    is_full=additional_chambers[pos].is_full,
                    real_administration_time=additional_chambers[pos].real_administration_time
                )
            )
        response = self.client.get(self.chambers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 40)
        self.assertEqual(response.data, expected_data)
    

    def test_chamber_retrieve(self):
        chambers = Chamber.objects.filter(container=self.container.uuid)
        expected_data = OrderedDict(
            uuid=str(chambers[0].uuid),
            position=chambers[0].position,
            is_full=chambers[0].is_full,
            real_administration_time=chambers[0].real_administration_time
        )
        response = self.client.get(
            self.chambers_url + f"/{chambers[0].uuid}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
