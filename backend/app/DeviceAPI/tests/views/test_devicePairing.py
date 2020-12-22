from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from DeviceAPI.models import (
    Device,
    DeviceVersion,
    PairingInfo
)


class DevicePairingTestCase(APITestCase):
    pairingInfo_post_url = "/api/pairing/"
    pairingInfoVerify_get_url = "/api/pairing/verify/"

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
        data = {
            "serial_number": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "hardware_version": "0.0",
            "firmware_version": "0.0.0"
        }

        response = self.client.post(
            self.pairingInfo_post_url,
            data,
            format="json"
        )

        expected_data = {
            "pairing_code": PairingInfo.objects.first().pairing_code
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)

    def test_pairingVerify(self):
        self.pairing_info = PairingInfo.objects.create(
            pairing_code=PairingInfo.generate_code(),
            serial_number="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            hardware_version="0.0",
            firmware_version="0.0.0"
        )
        response = self.client.get(
            self.pairingInfoVerify_get_url + str(self.pairing_info.pairing_code),
            format="json"
        )

        token = Token.objects.first()
        expected_data = {
            "api_token": token.key,
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
