"""
Code for device pairing API.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "25.5.2020" 

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from DeviceAPI.models import Device, DeviceApiToken, DevicePairingKey
from django.conf import settings
from datetime import datetime,timedelta
import secrets

class RequestKeys(APIView):
    """
    Generate pairing keys.
    """
    
    parser_classes = [JSONParser]
    
    def get(self, request, format=None):
        # check if the device with the given UUID is in the database
        # if device is not present in the database then add a new one
        device = Device.objects.filter(serialNumber__exact=request.data["serial_no"])
        if device.count() == 0:
            device = Device(serialNumber=request.data["serial_no"])
            device.save()
        else:
            device = device[0]
        
        # check if any tokens are assigned to the current device
        # if they are then delete them
        for token in DeviceApiToken.objects.filter(device__exact=device).all():
            token.delete()
        
        for token in DevicePairingKey.objects.filter(device__exact=device).all():
            token.delete()
        
        # generate new unique token
        while True:
            token = secrets.token_urlsafe(30)
            if DeviceApiToken.objects.filter(token__exact=token).count() == 0:
                break
        
        # generate new unique code
        while True:
            code = '{n:05d}'.format(n=secrets.randbelow(10**6))
            if DevicePairingKey.objects.filter(key__exact=code).count() == 0:
                break
        
        # add new API token and new device Pairing key to DB
        DeviceApiToken(token=token,
                       device=device).save()

        DevicePairingKey(key=code,
                         expires=datetime.now()+timedelta(minutes=settings.PAIRING_CODE_LIFETIME),
                         device=device).save()
        
        # build and return response
        return Response({'code': code, 'token': token})
