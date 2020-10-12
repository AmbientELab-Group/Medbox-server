from rest_framework import serializers
from DeviceAPI.models import Device
from rest_framework.validators import UniqueTogetherValidator


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "uuid",
            "owner",
            "capacity",
            "name",
            "fillStatus"
        ]
        read_only_fields = [
            "fillStatus"
        ]
        validators = [
            # check name uniqueness
            UniqueTogetherValidator(
                queryset=Device.objects.all(),
                fields=["name", "owner"]
            )
        ]
