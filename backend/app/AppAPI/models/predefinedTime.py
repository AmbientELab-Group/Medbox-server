
__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID
from django.contrib.auth import get_user_model

class PredefinedTime(models.Model):
    """
    Model of the predefined administration times.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to the owner of this object
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="predefinedTimes")

    # administration time
    time = models.DateTimeField()

    # custom name of this time
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"'{self.name}' at: {self.time}"
