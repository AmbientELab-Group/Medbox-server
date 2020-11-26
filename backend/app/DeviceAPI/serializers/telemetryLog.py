from rest_framework import serializers
from DeviceAPI.models import TelemetryLog


class TelemetrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TelemetryLog
        fields = [
            "uuid",
            "timestamp",
            "signal_strength",
            "battery_status",
            "battery_voltage",
            "device_status",
        ]