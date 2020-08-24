"""
Device pairing key.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "25.5.2020"

from django.db import models
from .device import Device

class DevicePairingKey(models.Model):
    """
    Model of the key used for paring of the device.
    """
    # key itself
    key = models.CharField(max_length=6)
    
    # device to which the key is assigned
    device = models.OneToOneField(Device, on_delete=models.PROTECT)
    
    # expiration time
    expires = models.DateTimeField()
