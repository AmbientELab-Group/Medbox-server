"""
Model of the chamber.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID

class Chamber(models.Model):
    """
    Model of the chamber.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to doses stored in this chamber
    doses = models.ManyToManyField("AppAPI.Dose")

    # position in the container
    position = models.PositiveSmallIntegerField()

    # indicates if the chamber is empty
    isFull = models.BooleanField(default=True)

    # time of administration its content
    realAdministrationTime = models.DateTimeField(null=True)
