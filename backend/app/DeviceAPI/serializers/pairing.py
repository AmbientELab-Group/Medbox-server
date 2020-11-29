from rest_framework import serializers
from DeviceAPI.models import PairingInfo
from rest_framework.validators import UniqueTogetherValidator


class PairingInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PairingInfo
        fields = [
            "serial_number",
            "hardware_version",
            "firmware_version",
        ]
        
        read_only_fields = ["pairing_code"]


        
