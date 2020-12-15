from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from DeviceAPI.models import (
    Device,
    DeviceVersion,
    PairingInfo
)
from uuid import UUID
from collections import OrderedDict


class DevicePairingTestCase(APITestCase):
    #url declaration
    pairingInfo_post_url = "/api/pairing/"

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
    
    def test_pairingInfo_create(self):
        test_serialnum = "3fa85f64-5717-4562-b3fc-2c963f66afa6"

        data = {
            "serial_number": test_serialnum,
            "hardware_version": self.device_version.name,
            "firmware_version": self.device_version.latest_firmware_version
        }

        response = self.client.post(
            self.pairingInfo_post_url,
            data,
            format="json"
        )

        expected_data = (
            "pairing_code": pairingInfo.objects.get(position=1).pairing_code
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_pairingVerify(self):
        pass
