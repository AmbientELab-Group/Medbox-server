"""
Model of the predefined administration times.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID

class PredefinedTime(models.Model):
    """
    Model of the predefined administration times.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # custom name of this time
    name = models.CharField(max_length=100, default="")

    # administration time
    time = models.DateTimeField()

    def __str__(self):
        return f"'{self.name}' at: {self.time}"