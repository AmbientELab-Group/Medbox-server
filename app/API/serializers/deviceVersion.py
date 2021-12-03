from rest_framework import serializers
from API.models import DeviceVersion


class DeviceVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceVersion
        fields = [
            "name",
            "capacity",
            "latest_firmware_version"
        ]
        read_only_fields = [
            "name",
            "capacity",
            "latest_firmware_version"
        ]
