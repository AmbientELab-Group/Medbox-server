"""
Device access tokens.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "25.5.2020" 

from django.db import models
from .device import Device

class DeviceApiToken(models.Model):
    """
    Model of the device token for API.
    """
    # key itself
    token = models.CharField(max_length=42)
    
    # device to which the token is assigned
    device = models.OneToOneField(Device, on_delete=models.PROTECT)
