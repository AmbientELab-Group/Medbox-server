from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from DeviceAPI.models import (
    Device,
    deviceVersion,
    pairingInfo
)
from uuid import UUID
from collections import OrderedDict

