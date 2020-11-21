from rest_framework import serializers
from DeviceAPI.models import Device
from rest_framework.validators import UniqueTogetherValidator


class PairingGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = [
            #"uuid",  # just for testing puproses
            "pairing_code"

        ]
        validators = [
            # check name uniqueness
            UniqueTogetherValidator(
                queryset=Device.objects.all(),
                fields=["uuid"]
            )
        ] 
