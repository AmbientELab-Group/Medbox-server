from rest_framework import serializers
from DeviceAPI.models import ContainerVersion


class ContainerVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerVersion
        fields = [
            "name",
            "capacity"
        ]
        read_only_fields = [
            "name",
            "capacity"
        ]
