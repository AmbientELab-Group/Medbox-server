from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from DeviceAPI.models import (
    Chamber,
)
from DeviceAPI.serializers import ChamberSerializer
from uuid import UUID
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
        self.chambers = []
