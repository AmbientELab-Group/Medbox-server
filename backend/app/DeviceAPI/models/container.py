"""
Model of the container.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID
from django.utils import timezone

class Container(models.Model):
    """
    Model of the container.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to chambers of this container
    chambers = models.ManyToManyField("Chamber")

    # position in the container
    position = models.PositiveSmallIntegerField()

    # time this container was refilled at
    lastRefill = models.DateTimeField(default=timezone.now)
