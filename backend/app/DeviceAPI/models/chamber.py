"""
Constraints:
    - if real_administration_time is not null the chamber has been emptied
    and is_full needs to be False
    - there cannot be any other chamber at the same position in the
    same container
    - the position of the chamber cannot be greater than the capacity
    of the container
"""
from django.db import models
import uuid as UUID
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models import Q


class Chamber(models.Model):
    # universal identifier
    uuid = models.UUIDField(
        primary_key=True,
        default=UUID.uuid4,
        editable=False,
        unique=True
    )

    # reference to container this chamber belongs to
    container = models.ForeignKey(
        "Container",
        on_delete=models.CASCADE,
        related_name="chambers"
    )

    # position in the container
    position = models.PositiveSmallIntegerField()

    # indicates if the chamber is empty
    is_full = models.BooleanField(default=False)

    # time of administration of its content
    real_administration_time = models.DateTimeField(
        null=True,
        blank=True
    )

    def clean(self):
        # check if is_full and real_administration_time fields are in sync
        if self.real_administration_time is not None and self.is_full:
            raise ValidationError(
                _("The dose was administered but chamber is still full."),
                code="integrity_error"
            )

        # make sure there are no two chambers at the same position
        if Chamber.objects.filter(
            ~Q(uuid=self.uuid) &
            Q(container=self.container) &
            Q(position=self.position)
        ).exists():
            raise ValidationError(
                _("Two chambers at the same place."),
                code="integrity_error"
            )

        # validate if the position is in the correct range
        if self.position < 0 or self.position >= self.container.capacity:
            raise ValidationError(
                _("Position value outside of container's capacity."),
                code="invalid_value"
            )

    def __str__(self):
        return f"Container: {self.container} At position: {self.position}"
