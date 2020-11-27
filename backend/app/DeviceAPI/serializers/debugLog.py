from rest_framework import serializers
from DeviceAPI.models import DebugLog


class DebugLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebugLog
        fields = [
            "uuid",
            "severity",
            "message_code",
            "timestamp",
            "details"
        ]