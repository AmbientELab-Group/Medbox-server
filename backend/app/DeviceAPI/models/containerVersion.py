"""
Model of the container version.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID

class ContainerVersion(models.Model):
    """
    Model of the container version.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # name of this version
    name = models.CharField(max_length=100, unique=True)

    # number of chambers
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name}"