from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from DeviceAPI.models import (
    Device,
    DeviceToken,
    DeviceVersion,
    TelemetryLog
)


class TelemetryLogViewTestCase(APITestCase):
    telemetrylog_url = "/api/telemetry"

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
            key=DeviceToken.generate_key(),
            user=self.device
        )

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.device_token.key)

    def test_telemetry_create(self):
        data = {
            "timestamp": 1606409799,
            "battery_status": 0,
            "signal_strength": 0,
            "device_status": 0,
            "battery_voltage": 0
        }

        response = self.client.post(
            self.telemetrylog_url,
            data,
            format="json"
        )

        new_telemetrylog = TelemetryLog.objects.get(device=self.device)

        expected_data = {
            "device": self.device.uuid,
            "timestamp": 1606409799,
            "battery_status": 0,
            "signal_strength": 0,
            "device_status": 0,
            "battery_voltage": 0
        }

        data_from_model = {
            "device": new_telemetrylog.device.uuid,
            "timestamp": new_telemetrylog.timestamp,
            "battery_status": new_telemetrylog.battery_status,
            "signal_strength": new_telemetrylog.signal_strength,
            "device_status": new_telemetrylog.device_status,
            "battery_voltage": new_telemetrylog.battery_voltage
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data_from_model, expected_data)
