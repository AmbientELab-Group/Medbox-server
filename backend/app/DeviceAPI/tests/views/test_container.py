from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from DeviceAPI.models import (
    Container,
    ContainerVersion,
    Device,
    DeviceVersion
)
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
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(tokens.access_token))

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

    def test_container_list_all(self):
        expected_data = OrderedDict(
            uuid=str(self.container.uuid),
            version=self.container.version.name,
            device=UUID(str(self.container.device.uuid)),
            position=self.container.position,
            last_refill=self.container.last_refill,
            fill_status=self.container.fill_status
        )
        response = self.client.get(self.containers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0], expected_data)

    def test_container_create(self):
        data = {
            "device": self.device.uuid,
            "version": self.container_version.name
        }

        response = self.client.post(
            self.containers_url,
            data,
            format="json"
        )

        new_container = Container.objects.get(position=1)

        expected_data = {
            "uuid": str(new_container.uuid),
            "version": self.container_version.name,
            "device": self.device.uuid,
            "position": 1,
            "last_refill": None,
            "fill_status": 0
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)
