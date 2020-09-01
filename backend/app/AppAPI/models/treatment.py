"""
Model of the treatment.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID
from django.contrib.auth import get_user_model

class Treatment(models.Model):
    """
    Model of the treatment.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to the beneficiary of this treatment
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="treatments")

    # custom name of the treatment
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.name}"
