"""
Constraints:
    - planned_administration_time has to be set in the future
    - number_of_pills has to be positive
    - there can be either administration time or on demand option set, not
    both at the same time
"""
from django.db import models
import uuid as UUID
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils import timezone


def planned_administration_time_validator(time):
    if time < timezone.now():
        raise ValidationError(
            _("Choose administration time to be in the future."),
            code="invalid_value"
        )


def number_of_pills_validator(num_of_pills):
    if num_of_pills <= 0:
        raise ValidationError(
            _("Incorrect number of pills specified."),
            code="invalid_value"
        )


class Dose(models.Model):
    # universal identifier
    uuid = models.UUIDField(
        primary_key=True,
        default=UUID.uuid4,
        editable=False,
        unique=True
    )

    # reference to the treatment this dose belongs to
    treatment = models.ForeignKey(
        "Treatment",
        on_delete=models.CASCADE,
        related_name="doses"
    )

    # reference to chamber this dose is stored in
    chamber = models.ForeignKey(
        "DeviceAPI.Chamber",
        on_delete=models.SET_NULL,
        related_name="doses",
        null=True
    )

    # reference to medicine to administer
    medicine = models.ForeignKey(
        "Medicine",
        on_delete=models.PROTECT,
        related_name="doses"
    )

    # administration time
    planned_administration_time = models.DateTimeField(
        null=True,
        blank=True,
        validators=[planned_administration_time_validator]
    )

    # size of the dose
    number_of_pills = models.FloatField(validators=[number_of_pills_validator])

    # specifies if the dose is scheduled or available on demand
    on_demand = models.BooleanField(default=False)

    def clean(self):
        # check if the on_demand option do not collide with timestamp
        if self.planned_administration_time is None and self.on_demand is False:
            raise ValidationError(
                _("Choose administration time or specify on demand option."),
                code="integrity_error"
            )

        if self.planned_administration_time is not None and self.on_demand is True:
            raise ValidationError(
                _("Choose either administration time or on demand option."),
                code="integrity_error"
            )

    def __str__(self):
        return f"{self.medicine} at: {self.planned_administration_time}"
