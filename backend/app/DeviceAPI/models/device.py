"""
Constraints:
    - device name must be unique for a user
"""
from django.db import models
from django.contrib.auth import get_user_model
import uuid as UUID
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q


class Device(models.Model):
    # universal identifier
    uuid = models.UUIDField(
        primary_key=True,
        default=UUID.uuid4,
        editable=False,
        unique=True
    )

    # reference to owner of this device
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="ownedDevices"
    )

    # reference to supervisors of this device
    supervisors = models.ManyToManyField(
        get_user_model(),
        related_name="supervisedDevices"
    )

    # max number of containers which fit into this device
    capacity = models.PositiveSmallIntegerField()

    # name given to the device by user
    name = models.CharField(max_length=100)

    # pairing key used to connect the device with a user's account
    pairing_key = models.CharField(
        max_length=6,
        default=''
    )

    # pairing key expiration date
    pairing_key_expires_at = models.DateTimeField(null=True)

    # token used to authenticated API calls from this device
    api_token = models.CharField(
        max_length=42,
        default=''
    )

    def fill_status(self):
        """
        Returns number of percents this device is filled in calculated over
        every container inside.
        """
        containers = self.containers.filter(device=self)
        totalCapacity = 0
        fullChambers = 0
        for cont in containers:
            totalCapacity += cont.capacity
            chambers = cont.chambers.filter(container=cont)
            for chamb in chambers:
                if chamb.is_full:
                    fullChambers += 1

        if totalCapacity == 0:
            return 0

        return round(100 * fullChambers / totalCapacity)

    def clean(self):
        # check name uniqueness
        if Device.objects.filter(
            Q(owner=self.owner) &
            Q(name=self.name)
        ).exists():
            raise ValidationError(
                _("Device with this name already exists, choose different name."),
                code="duplicated_value"
            )

    def __str__(self):
        return f"'{self.name}':{self.uuid}"
