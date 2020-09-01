"""
Model of the container.
Constraints:
    - the position of the container has to be in range of device capacity based on device version
    - on creation it needs to create entries for each of its chambers
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

##############
# Validators #
##############

# integrity check
def cleanContainer(self):
    # validate if the position is in the correct range
    if self.position < 0 or self.position >= self.device.version.capacity:
        raise ValidationError(_("Position value outside of container's capacity"), code="invalid_value")

    # create chamber entities if needed
    if not Container.objects.filter(uuid=self.uuid).exists():
        print("No container like this")
        for pos in range(self.version.capacity):
            c = Chamber(container=self, position=pos)
            c.save()


class Container(models.Model):
    """
    Model of the container.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to the version of this device
    version = models.ForeignKey("ContainerVersion", on_delete=models.PROTECT, related_name="containers")

    # reference to device this container belongs to
    device = models.ForeignKey("Device", on_delete=models.CASCADE, related_name="containers")

    # position in the container
    position = models.PositiveSmallIntegerField()

    # time this container was refilled at
    lastRefill = models.DateTimeField(null=True ,blank=True)

    def clean(self):
        cleanContainer(self)

    def __str__(self):
        return f"At position: {self.position}, last refilled: {self.lastRefill}"
