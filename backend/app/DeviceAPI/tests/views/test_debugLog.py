from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from DeviceAPI.models import (
    Device,
    DeviceToken,
    DeviceVersion,
    DebugLog
)


class DebugViewTestCase(APITestCase):
    debug_url = "/api/debug/logs"
    token = "123456"

    def setUp(self):
        self.owner = get_user_model().objects.create(
            email="testemail@test.com",
            password="testpassword"
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

        self.device_token = DeviceToken.objects.create(
            key=self.token,
            user=self.device
        )

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

    def test_telemetry_create(self):
        data = {
            "severity": 1,
            "message_code": 0,
            "timestamp": 0,
            "details": "dupa"
        }

        response = self.client.post(
            self.debug_url,
            data,
            format="json"
        )

        new_debug = DebugLog.objects.get(device=self.device)

        expected_data = {
            "device": self.device.uuid,
            "severity": 1,
            "message_code": 0,
            "timestamp": 0,
            "details": "dupa"
        }

        data_from_model = {
            "device": new_debug.device.uuid,
            "severity": new_debug.severity,
            "message_code": new_debug.message_code,
            "timestamp": new_debug.timestamp,
            "details": new_debug.details
        }
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data_from_model, expected_data)
