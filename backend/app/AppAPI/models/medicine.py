"""
Model of the medicine.
Constraints:
    - there are no two same entries in this table (no two matching name AND producer entries)
      if the producer is empty the name has to be unique
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

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

    def clean(self):
        self.name = self.name.capitalize()
        isNameAlreadyUsed = Medicine.objects.filter(name=self.name).exists()

        if self.producer == "" and isNameAlreadyUsed:
            raise ValidationError(_("Medicine with this name already exists."), code="already_exists")

        self.producer = self.producer.capitalize()
        isProducerAlreadyUsed = Medicine.objects.filter(producer=self.producer).exists()

        if isNameAlreadyUsed and isProducerAlreadyUsed:
            raise ValidationError(_("Medicine with this name and producer already exists."), code="already_exists")

    def __str__(self):
        return f"{self.name} : {self.producer}"