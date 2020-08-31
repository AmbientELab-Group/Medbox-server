"""
Model of the medicine.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID

class Medicine(models.Model):
    """
    Model of the medicine.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # name of the medicine
    name = models.CharField(max_length=100, default="")

    # producer of the medicine, not required for now
    producer = models.CharField(max_length=100, default="", blank=True)

    def __str__(self):
        return f"{self.name} : {self.producer}"