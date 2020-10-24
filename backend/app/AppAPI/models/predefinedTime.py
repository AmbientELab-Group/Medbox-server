
__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models
import uuid as UUID
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q


class PredefinedTime(models.Model):
    """
    Model of the predefined administration times.
    """
    # universal identifier
    uuid = models.UUIDField(
        primary_key=True,
        default=UUID.uuid4,
        editable=False,
        unique=True
    )

    # reference to the owner of this object
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="predefinedTimes"
    )

    # administration time
    time = models.TimeField()

    # custom name of this time
    name = models.CharField(max_length=100)

    def clean(self):
        # check name uniqueness
        if PredefinedTime.objects.filter(Q(owner=self.owner) & Q(name=self.name)).exists():
            raise ValidationError(
                _("Predefined time with this name already exists, choose different name."),
                code="duplicated_value"
            )

    def __str__(self):
        return f"'{self.name}' at: {self.time}"
