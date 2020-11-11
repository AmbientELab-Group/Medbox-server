from rest_framework import serializers
from DeviceAPI.models import Chamber
from django.utils.translation import gettext as _
from rest_framework.validators import UniqueTogetherValidator


class ChamberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamber
        fields = [
            "uuid",
            "position",
            "is_full",
            "real_administration_time"
        ]
        validators = [
            # make sure there are no two chambers at the same place
            UniqueTogetherValidator(
                queryset=Chamber.objects.all(),
                fields=["container", "position"]
            )
        ]

    def validate_is_full(self):
        """
        Check if chamber is empty if administration time exists
        """
        if self.real_administration_time is not None and self.is_full:
            raise serializers.ValidationError(
                _("The dose was administered but chamber is still full."),
                code="integrity_error"
            )

    # assert position in capacity range
    def validate_position(self):
        if self.position < 0 or self.position >= self.container.capacity:
            raise serializers.ValidationError(
                _("Position value outside of container's capacity."),
                code="invalid_value"
            )
