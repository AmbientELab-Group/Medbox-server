"""
Model of the chamber.
Constraints:
    - if realAdministrationTime is not null the chamber has been emptied and isFull needs to be set to False
    - there cannot be any other chamber at the same position in the same container
    - the position of the chamber cannot be greater than the capacity of the container
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020"

from django.db import models
import uuid as UUID
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q

##############
# Validators #
##############

# integrity check
def cleanChamber(self):
    # change isFull to false if the dose was administered
    if self.realAdministrationTime is not None and self.isFull:
            self.isFull = False

    # make sure there are no two chambers at the same place
    if Chamber.objects.filter(Q(container=self.container) & Q(position=self.position)).exists():
        raise ValidationError(_("Two chambers in the same place."), code="integrity_error")

    # validate if the position is in the correct range
    if self.position < 0 or self.position >= self.container.version.capacity:
        raise ValidationError(_("Position value outside of container's capacity"), code="invalid_value")

    
class Chamber(models.Model):
    """
    Model of the chamber.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to container this chamber belongs to
    container = models.ForeignKey("Container", on_delete=models.CASCADE, related_name="chambers")

    # position in the container
    position = models.PositiveSmallIntegerField()

    # indicates if the chamber is empty
    isFull = models.BooleanField(default=False)

    # time of administration of its content
    realAdministrationTime = models.DateTimeField(null=True, blank=True)
    
    # validation
    def clean(self):
        cleanChamber(self)

    def __str__(self):
        return f"At position: {self.position}, admin. time: {self.realAdministrationTime}"
