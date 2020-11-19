from rest_framework.authentication import TokenAuthentication
from ..models import DeviceToken


class DeviceTokenAuthentication(TokenAuthentication):
    model = DeviceToken
