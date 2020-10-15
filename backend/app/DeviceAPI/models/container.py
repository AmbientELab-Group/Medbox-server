"""
Constraints:
    - the position of the container has to be in range of device capacity
    based on device version
    - on creation it checks there is a proper amount of chambers associated
    with this object
    - there cannot be any other container at the same place in the same device
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020"

from django.db import models
import uuid as UUID
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q


class Container(models.Model):
    # universal identifier
    uuid = models.UUIDField(
        primary_key=True,
        default=UUID.uuid4,
        editable=False,
        unique=True
    )

    # number of chambers in this container
    capacity = models.PositiveSmallIntegerField()

    # reference to device this container belongs to
    device = models.ForeignKey(
        "Device",
        on_delete=models.CASCADE,
        related_name="containers"
    )

    # position in the container
    position = models.PositiveSmallIntegerField()

    # time this container was refilled at
    lastRefill = models.DateTimeField(null=True, blank=True)

    def fillStatus(self):
        chambers = self.chambers.filter(container=self)
        totalCapacity = self.capacity
        fullChambers = 0
        for chamb in chambers:
            if chamb.isFull:
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
        return f"In device: {self.device}, at pos. {self.position}, last refilled: {self.lastRefill}"
