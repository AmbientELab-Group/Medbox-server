"""
Device model.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "25.5.2020"

from django.db import models
from django.contrib.auth import get_user_model
import uuid as UUID
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q

##############
# Validators #
##############

def cleanDevice(self):
    # check name uniqueness
    if Device.objects.filter(Q(owner=self.owner) & Q(name=self.name)).exists():
        raise ValidationError(_("Device with this name already exists, choose different name."), code="duplicated_value")


class Device(models.Model):
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to owner of this device
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="ownedDevices")
    
    # reference to the version of this device
    version = models.ForeignKey("DeviceVersion", on_delete=models.PROTECT, related_name="devices")

    # name given to the device by user
    name = models.CharField(max_length=100)

    # pairing key used to connect the device with a user's account
    pairingKey = models.CharField(max_length=6, default='')

    # pairing key expiration date
    pairingKeyExpiresAt = models.DateTimeField(null=True)

    # token used to authenticated API calls from this device
    apiToken = models.CharField(max_length=42, default='')

    def clean(self):
        cleanDevice(self);

    def __str__(self):
        return f"'{self.name}' with id: {self.uuid}"
