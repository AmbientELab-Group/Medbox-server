from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from DeviceAPI.models import (
    Device,
    deviceVersion,
    PairingInfo
)
from uuid import UUID
from collections import OrderedDict

class DeviceTestCase(APITestCase):
    device_pairing_url = "/api/devices/pairing/confirm/"

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

        self.pairing_info = pairingInfo.objects.create(
            pairing_code = pairingInfo.generate_code()
            #serial_number = 
            #hardware_version = 
            #firmware_version
        )

    def test_pairing_confirm(self):
        data = {
            "device_uuid": self.device.uuid
            "pairing_code": self.pairing_info.pairing_code
        }
        response = self.client.post(
            self.device_pairing_url,
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)