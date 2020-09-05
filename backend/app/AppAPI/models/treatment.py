__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q

class Treatment(models.Model):
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)

    # reference to the beneficiary of this treatment
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="treatments")

    # custom name of the treatment
    name = models.CharField(max_length=100)

    def clean(self):
        if Treatment.objects.filter(Q(patient=self.patient) & Q(name=self.name)).exists():
            raise ValidationError(_("Treatment with this name already exists, choose different name."), code="duplicated_value")

    def __str__(self):
        return f"{self.name}"
