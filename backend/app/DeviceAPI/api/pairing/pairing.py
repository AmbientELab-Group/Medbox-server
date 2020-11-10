"""
Device pairing API.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from DeviceAPI.models import Device
from django.conf import settings
from datetime import datetime, timedelta, timezone
import secrets


class RequestKeys(APIView):
    """
    Generate pairing key and api_token for requesting device.

    For the first call made by any given device, this device is added to database and api_token is
    generated for it. Upon each subsequent call, new pairing code together with NEW APITOKEN are 
    generated and sent to calling device. New api_token is stored in the database and the old one
    is no longer valid, hence calling this endpoint invalidates previously established connection.
    """
    
    parser_classes = [JSONParser]
    
    def post(self, request, format=None):
        # check if the device with the given UUID is in the database
        # if device is not present in the database then add a new one
        device = Device.objects.filter(serialNumber__exact=request.data["serial_no"])

        # generate new unique code and expiration date
        while True:
            code = '{n:05d}'.format(n=secrets.randbelow(10**6))
            if Device.objects.filter(pairing_key__exact=code).count() == 0:
                expirationDate = datetime.now(timezone.utc)+timedelta(minutes=settings.PAIRING_CODE_LIFETIME)
                break

        # generate new unique api_token
        while True:
            token = secrets.token_urlsafe(30)
            if Device.objects.filter(api_token__exact=token).count() == 0:
                break

        if device.count() == 0:
            # create new device entry
            device = Device(serialNumber=request.data["serial_no"], 
                        api_token=token,
                        pairing_key=code,
                        pairing_key_expires_at=expirationDate)
        else:
            # update existing device entry with new api_token, pairing code and its expiration date
            device = device[0]
            device.pairing_key = code
            device.pairing_key_expires_at = expirationDate
            device.api_token = token

        device.save()

        # build and return response
        return Response({'code': code, 'token': token})
