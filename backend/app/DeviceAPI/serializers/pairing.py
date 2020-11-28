from rest_framework import serializers
from DeviceAPI.models import PairingInfo
from rest_framework.validators import UniqueTogetherValidator


class PairingInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PairingInfo
        fields = "__all__"
        
