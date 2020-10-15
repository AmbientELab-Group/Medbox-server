from rest_framework import serializers
from django.utils.translation import gettext as _
from rest_framework.validators import UniqueTogetherValidator
from DeviceAPI.models import Device, Container, Chamber


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

    # after creating container, create and bind its chambers
    # auto sets position based on existing containers
    def create(self, validated_data):
        container = Container.objects.create(**validated_data)
        for pos in range(validated_data.get("capacity")):
            Chamber.objects.create(container=container, position=pos)
        return container

    # adds createOnly behavior to capacity field
    def update(self, instance, validated_data):
        validated_data.pop("capacity", None)
        return super().update(instance, validated_data)

    # assert position in capacity range
    def validate_position(self, position):
        data = self.context.get("request").data
        deviceUUID = data.get("device")
        if deviceUUID:
            device = Device.objects.get(uuid=deviceUUID)
            if position < 0 or position >= device.capacity:
                raise serializers.ValidationError(
                    _("Position value outside of container's capacity."),
                    code="invalid_value"
                )
        return position

    # assert only the managed device can be set
    def validate_device(self, device):
        user = self.context.get("request").user
        supervisedDevices = user.supervisedDevices.all()
        if device in supervisedDevices or user == device.owner:
            return device

        raise serializers.ValidationError(
                _("Container cannot be assigned to this device."),
                code="forbidden_action"
            )
