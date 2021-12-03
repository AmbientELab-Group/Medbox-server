"""
Constraints:
    - the position of the container has to be in range of device capacity
    based on device version
    - on creation it checks there is a proper amount of chambers associated
    with this object
    - there cannot be any other container at the same place in the same device
"""
from django.db import models
import uuid as UUID
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q
from API.managers import ContainerManager


class Container(models.Model):
    # universal identifier
    uuid = models.UUIDField(
        primary_key=True,
        default=UUID.uuid4,
        editable=False,
        unique=True
    )

    # version that specifies capacity
    version = models.ForeignKey(
        "ContainerVersion",
        on_delete=models.PROTECT,
        related_name="existing_containers"
    )

    # reference to device this container belongs to
    device = models.ForeignKey(
        "Device",
        on_delete=models.CASCADE,
        related_name="containers"
    )

    # position in the container
    position = models.PositiveSmallIntegerField()

    # time this container was refilled at
    last_refill = models.DateTimeField(null=True, blank=True)

    # custom manager
    objects = ContainerManager()

    @property
    def capacity(self):
        return self.version.capacity

    @property
    def fill_status(self):
        """
        Returns number of percents this container is filled in calculated over
        every chamber inside.
        """
        chambers = self.chambers.filter(container=self)
        totalCapacity = self.capacity
        fullChambers = 0
        for chamb in chambers:
            if chamb.is_full:
                fullChambers += 1

        if totalCapacity == 0:
            return 0

        return round(100 * fullChambers / totalCapacity)

    def clean(self):
        # validate if the position is in the correct range
        if self.position < 0 or self.position >= self.device.capacity:
            raise ValidationError(
                _("Position value outside of container's capacity"),
                code="invalid_value"
            )

        # make sure there are no two containers at the same place
        if Container.objects.filter(
            ~Q(uuid=self.uuid) &
            Q(device=self.device) &
            Q(position=self.position)
        ).exists():
            raise ValidationError(
                _("Two containers at the same place."),
                code="integrity_error"
            )

    def __str__(self):
        return f"In {self.device}, at pos. {self.position}"
