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

    # reference to device this container belongs to
    device = models.ForeignKey("Device", on_delete=models.CASCADE, related_name="containers")

    # position in the container
    position = models.PositiveSmallIntegerField()

    # time this container was refilled at
    lastRefill = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"At position: {self.position}, last refilled: {self.lastRefill}"
