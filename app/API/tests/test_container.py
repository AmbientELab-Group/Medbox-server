from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from API.models import (
    Container,
    ContainerVersion,
    Device,
    DeviceVersion
)
from API.serializers import ContainerSerializer
from uuid import UUID
from collections import OrderedDict


class ContainerViewTestCase(APITestCase):
    containers_url = "/api/containers"

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

        self.containers = []

        for position in range(3):
            self.containers.append(
                Container.objects.create_with_chambers(
                    version=self.container_version,
                    device=self.device,
                    position=position
                )
            )

        self.additional_device = Device.objects.create(
            owner=self.owner,
            version=self.device_version,
            name="TestBox2"
        )

        self.additional_containers = []

        for position in range(2):
            self.additional_containers.append(
                Container.objects.create_with_chambers(
                    version=self.container_version,
                    device=self.additional_device,
                    position=position
                )
            )

    def test_container_list_all(self):
        expected_data = []

        for pos in range(3):
            expected_data.append(
                OrderedDict(
                    uuid=str(self.containers[pos].uuid),
                    version=self.containers[pos].version.name,
                    device=UUID(str(self.containers[pos].device.uuid)),
                    position=self.containers[pos].position,
                    last_refill=self.containers[pos].last_refill,
                    fill_status=self.containers[pos].fill_status
                )
            )

        for pos in range(2):
            expected_data.append(
                OrderedDict(
                    uuid=str(self.additional_containers[pos].uuid),
                    version=self.additional_containers[pos].version.name,
                    device=UUID(str(self.additional_containers[pos].device.uuid)),
                    position=self.additional_containers[pos].position,
                    last_refill=self.additional_containers[pos].last_refill,
                    fill_status=self.additional_containers[pos].fill_status
                )
            )

        response = self.client.get(self.containers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data, expected_data)

    def test_container_list_from_device(self):
        expected_data = []

        for pos in range(3):
            expected_data.append(
                OrderedDict(
                    uuid=str(self.containers[pos].uuid),
                    version=self.containers[pos].version.name,
                    device=UUID(str(self.containers[pos].device.uuid)),
                    position=self.containers[pos].position,
                    last_refill=self.containers[pos].last_refill,
                    fill_status=self.containers[pos].fill_status
                )
            )

        response = self.client.get(
            self.containers_url + f"?device={self.device.uuid}"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data, expected_data)

    def test_container_create(self):
        data = {
            "device": self.additional_device.uuid,

            "version": self.container_version.name
        }

        response = self.client.post(
            self.containers_url,
            data,
            format="json"
        )

        new_container = Container.objects.get(
            device=self.additional_device.uuid,
            position=2
        )

        expected_data = {
            "uuid": str(new_container.uuid),
            "version": self.container_version.name,
            "device": self.additional_device.uuid,
            "position": 2,
            "last_refill": None,
            "fill_status": 0
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)

    def test_container_create_with_shift(self):
        input_data = {
            "device": self.additional_device.uuid,
            "version": self.container_version.name,
            "position": 0
        }

        expected_containers = []

        for pos in range(2):
            expected_containers.append(
                OrderedDict(
                    uuid=str(self.additional_containers[pos].uuid),
                    version=self.additional_containers[pos].version.name,
                    device=UUID(str(self.additional_containers[pos].device.uuid)),
                    position=self.additional_containers[pos].position + 1,
                    last_refill=self.additional_containers[pos].last_refill,
                    fill_status=self.additional_containers[pos].fill_status
                )
            )

        response = self.client.post(
            self.containers_url,
            input_data,
            format="json"
        )

        new_container = Container.objects.get(
            device=self.additional_device.uuid,
            position=0
        )

        expected_data = {
            "uuid": str(new_container.uuid),
            "version": self.container_version.name,
            "device": self.additional_device.uuid,
            "position": 0,
            "last_refill": None,
            "fill_status": 0
        }

        expected_containers.append(OrderedDict(expected_data))

        final_containers = Container.objects.filter(
            device=self.additional_device.uuid
        )

        serializer = ContainerSerializer(final_containers, many=True)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(serializer.data, expected_containers)

    def test_container_retrive(self):
        expected_data = OrderedDict(
            uuid=str(self.containers[0].uuid),
            version=self.containers[0].version.name,
            device=UUID(str(self.containers[0].device.uuid)),
            position=self.containers[0].position,
            last_refill=self.containers[0].last_refill,
            fill_status=self.containers[0].fill_status
        )

        response = self.client.get(
            self.containers_url + f"/{self.containers[0].uuid}"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_container_update(self):
        expected_data = OrderedDict(
            uuid=str(self.containers[0].uuid),
            version=self.containers[0].version.name,
            device=UUID(str(self.additional_device.uuid)),
            position=0,
            last_refill=self.containers[0].last_refill,
            fill_status=self.containers[0].fill_status
        )

        input_data = OrderedDict(
            device=UUID(str(self.additional_device.uuid)),
            position=0
        )

        expected_containers = []

        expected_containers.append(OrderedDict(expected_data))

        for pos in range(2):
            expected_containers.append(
                OrderedDict(
                    uuid=str(self.additional_containers[pos].uuid),
                    version=self.additional_containers[pos].version.name,
                    device=UUID(str(self.additional_containers[pos].device.uuid)),
                    position=self.additional_containers[pos].position + 1,
                    last_refill=self.additional_containers[pos].last_refill,
                    fill_status=self.additional_containers[pos].fill_status
                )
            )

        response = self.client.put(
            self.containers_url + f"/{self.containers[0].uuid}",
            input_data,
            format="json"
        )

        # check if containers in additional device reorganized themself
        final_containers = Container.objects.filter(
            device=self.additional_device.uuid
        )
        serializer = ContainerSerializer(final_containers, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(serializer.data, expected_containers)

    def test_container_destroy(self):
        expected_containers = []

        for pos in range(1, 3):
            expected_containers.append(
                OrderedDict(
                    uuid=str(self.containers[pos].uuid),
                    version=self.containers[pos].version.name,
                    device=UUID(str(self.containers[pos].device.uuid)),
                    position=self.containers[pos].position - 1,
                    last_refill=self.containers[pos].last_refill,
                    fill_status=self.containers[pos].fill_status
                )
            )

        response = self.client.delete(
            self.containers_url + f"/{self.containers[0].uuid}"
        )

        final_containers = Container.objects.filter(
            device=self.device.uuid
        )
        serializer = ContainerSerializer(final_containers, many=True)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(serializer.data, expected_containers)
