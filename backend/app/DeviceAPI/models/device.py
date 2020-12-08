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
        related_name="supervisedDevices",
        blank=True
    )

    # based on django user model field
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this device should be treated as active. "
            "Unselect this instead of deleting device object."
        ),
    )

    # version that specifies capacity and latest firmware version
    version = models.ForeignKey(
        "DeviceVersion",
        on_delete=models.PROTECT,
        related_name="existing_devices"
    )

    # name given to the device by user
    name = models.CharField(max_length=100)

    # factory serial number assigned to the device
    serial_number = models.UUIDField(
        null=True,
        blank=True
    )

    # version of the hardware
    hardware_version = models.CharField(
        max_length=11,
        default="",
        blank=True
    )

    # version of the firmware
    firmware_version = models.CharField(
        max_length=11,
        default="",
        blank=True
    )

    @property
    def capacity(self):
        return self.version.capacity

    @property
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
            ~Q(uuid=self.uuid) &
            Q(owner=self.owner) &
            Q(name=self.name)
        ).exists():
            raise ValidationError(
                _("Device with this name already exists, choose different name."),
                code="duplicated_value"
            )

    def is_managed(self, user):
        """
        Checks if user is the owner or supervisor of this device.
        """
        return self.owner == user or user in self.supervisors.all()

    # for compatibility sake, copy pasted from django source, don't ask
    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def __str__(self):
        return f"'{self.name}':{self.uuid}"
