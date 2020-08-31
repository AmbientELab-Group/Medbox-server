"""
Model of the dose.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID

class Dose(models.Model):
    """
    Model of the dose.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to chamber this dose is stored in
    chamber = models.ForeignKey("DeviceAPI.Chamber", on_delete=models.SET_NULL, related_name="doses", null=True)

    # reference to medicine to administer
    medicine = models.ForeignKey("Medicine", on_delete=models.PROTECT, related_name="doses")

    # administration time
    plannedAdministrationTime = models.DateTimeField(null=True, blank=True)

    # size of the dose
    numberOfPills = models.FloatField()

    # specifies if the dose is scheduled or available on demand
    onDemand = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.medicine} at: {self.plannedAdministrationTime}"