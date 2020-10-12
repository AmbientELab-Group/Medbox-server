from rest_framework import serializers
from DeviceAPI.models import Container
from django.utils.translation import gettext as _
from rest_framework.validators import UniqueTogetherValidator


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = [
            "uuid",
            "capacity",
            "device",
            "position",
            "lastRefill",
            "fillStatus"
        ]
        read_only_fields = [
            "fillStatus"
        ]
        validators = [
            # assert position uniqueness
            UniqueTogetherValidator(
                queryset=Container.objects.all(),
                fields=["position", "device"]
            )
        ]

    # assert position in capacity range
    def validate_position(self):
        if self.position < 0 or self.position >= self.device.capacity:
            raise serializers.ValidationError(
                _("Position value outside of container's capacity."),
                code="invalid_value"
            )
