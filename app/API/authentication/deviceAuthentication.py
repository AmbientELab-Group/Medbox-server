from rest_framework.authentication import TokenAuthentication
from API.models import DeviceToken


class DeviceTokenAuthentication(TokenAuthentication):
    model = DeviceToken
