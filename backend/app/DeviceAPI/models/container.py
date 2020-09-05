"""
Constraints:
    - the position of the container has to be in range of device capacity based on device version
    - on creation it checks there is a proper amount of chambers associated with this object
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q
from .chamber import Chamber


class Container(models.Model):
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # number of chambers in this container
    capacity = models.PositiveSmallIntegerField()

    # reference to device this container belongs to
    device = models.ForeignKey("Device", on_delete=models.CASCADE, related_name="containers")

    # position in the container
    position = models.PositiveSmallIntegerField()

    # time this container was refilled at
    lastRefill = models.DateTimeField(null=True ,blank=True)

    def clean(self):
        # validate if the position is in the correct range
        if self.position < 0 or self.position >= self.device.capacity:
            raise ValidationError(_("Position value outside of container's capacity"), code="invalid_value")

         # check if the chamber entities are associated with this container
        numberOfConainers = Container.objects.filter(uuid=self.uuid).count()
        if numberOfConainers != self.capacity:
            raise ValidationError(_("Chambers not instantiated"), code="integrity_error")

    def __str__(self):
        return f"At position: {self.position}, last refilled: {self.lastRefill}"
