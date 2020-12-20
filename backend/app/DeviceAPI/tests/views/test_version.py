from rest_framework.test import APITestCase
from rest_framework import status
from DeviceAPI.models import (
    ContainerVersion,
    DeviceVersion
)
from collections import OrderedDict

class DeviceVersionViewTestCase(APITestCase):
    device_versions_url = "/api/versions/device"

    def setUp(self):
        self.device_version_1 = DeviceVersion.objects.create(
            name="1.0",
            capacity=10,
            latest_firmware_version="1.0.1"
        )

        self.device_version_2 = DeviceVersion.objects.create(
            name="2.0",
            capacity=20,
            latest_firmware_version="2.0.1"
        )

        self.device_version_3 = DeviceVersion.objects.create(
            name="3.0",
            capacity=30,
            latest_firmware_version="3.0.1"
        )

    def test_device_versions_list_all(self):
        expected_data = [
            OrderedDict(
                name=self.device_version_1.name,
                capacity=self.device_version_1.capacity,
                latest_firmware_version=self.device_version_1.latest_firmware_version,
            ),
            OrderedDict(
                name=self.device_version_2.name,
                capacity=self.device_version_2.capacity,
                latest_firmware_version=self.device_version_2.latest_firmware_version,
            ),
            OrderedDict(
                name=self.device_version_3.name,
                capacity=self.device_version_3.capacity,
                latest_firmware_version=self.device_version_3.latest_firmware_version,
            )
        ]
        response = self.client.get(self.device_versions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0], expected_data[0])
        self.assertEqual(response.data[1], expected_data[1])
        self.assertEqual(response.data[2], expected_data[2])

class ContainerVersionViewTestCase(APITestCase):
    container_versions_url = "/api/versions/container"

    def setUp(self):
        self.container_version_1 = ContainerVersion.objects.create(
            name="1.0",
            capacity=10
        )

        self.container_version_2 = ContainerVersion.objects.create(
            name="2.0",
            capacity=20
        )

        self.container_version_3 = ContainerVersion.objects.create(
            name="3.0",
            capacity=30
        )

    def test_container_versions_list_all(self):
        expected_data = [
            OrderedDict(
                name=self.container_version_1.name,
                capacity=self.container_version_1.capacity
            ),
            OrderedDict(
                name=self.container_version_2.name,
                capacity=self.container_version_2.capacity
            ),
            OrderedDict(
                name=self.container_version_3.name,
                capacity=self.container_version_3.capacity
            )
        ]
        response = self.client.get(self.container_versions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0], expected_data[0])
        self.assertEqual(response.data[1], expected_data[1])
        self.assertEqual(response.data[2], expected_data[2])