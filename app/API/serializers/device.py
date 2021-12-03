from rest_framework import serializers
from API.models import Device
from rest_framework.validators import UniqueTogetherValidator


class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Device
        fields = [
            "uuid",
            "owner",
            "capacity",
            "name",
            "fill_status"
        ]
        read_only_fields = [
            "fill_status"
        ]
        validators = [
            # check name uniqueness
            UniqueTogetherValidator(
                queryset=Device.objects.all(),
                fields=["name", "owner"]
            )
        ]
