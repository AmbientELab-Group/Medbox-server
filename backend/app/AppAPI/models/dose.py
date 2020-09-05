"""
Constraints:
    - plannedAdministrationTime has to be set in the future
    - numberOfPills has to be positive
    - there can be either administration time or on demand option set, not both at the same time
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils import timezone

# new plannedAdministrationTimes need to be in the future
def plannedAdministrationTimeValidator(time):
    if time < timezone.now():
        raise ValidationError(_("Choose administration time to be in the future."), code="invalid_value")


# numberOfPills has to be positive
def numberOfPillsValidator(numOfPills):
    if numOfPills < 1:
        raise ValidationError(_("Incorrect number of pills specified."), code="invalid_value")


# validate integrity of the whole model
def cleanDose(self):
    # check if the onDemand option do not collide with timestamp
    if self.plannedAdministrationTime == None and self.onDemand == False:
        raise ValidationError(_("Choose administration time or specify on demand option."), code="integrity_error")

    if self.plannedAdministrationTime != None and self.onDemand == True:
        raise ValidationError(_("Choose either administration time or on demand option."), code="integrity_error")


class Dose(models.Model):
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to the treatment this dose belongs to
    treatment = models.ForeignKey("Treatment", on_delete=models.CASCADE, related_name="doses")

    # reference to chamber this dose is stored in
    chamber = models.ForeignKey("DeviceAPI.Chamber", on_delete=models.SET_NULL, related_name="doses", null=True)

    # reference to medicine to administer
    medicine = models.ForeignKey("Medicine", on_delete=models.PROTECT, related_name="doses")

    # administration time
    plannedAdministrationTime = models.DateTimeField(null=True, blank=True, validators=[plannedAdministrationTimeValidator])

    # size of the dose
    numberOfPills = models.FloatField(validators=[numberOfPillsValidator])

    # specifies if the dose is scheduled or available on demand
    onDemand = models.BooleanField(default=False)

    def clean(self):
        cleanDose(self)

    def __str__(self):
        return f"{self.medicine} at: {self.plannedAdministrationTime}"
