from rest_framework import serializers
from django.utils.translation import gettext as _
from rest_framework.validators import UniqueTogetherValidator
from DeviceAPI.models import Device, Container


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = [
            "uuid",
            "capacity",
            "device",
            "position",
            "last_refil",
            "fill_status"
        ]
        read_only_fields = [
            "capacity",
            "fill_status"
        ]

    def create(self, validated_data):
        """
        Assert this serializer is not used for create operation.
        """
        raise Exception("Create operation called from ContainerSerializer")

    def validate_position(self, position):
        """
        Check if position is in capacity range.
        """
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

    def validate_device(self, device):
        """
        Check if user has permissions to assign this container to the
        provided device.
        """
        user = self.context.get("request").user
        supervisedDevices = user.supervisedDevices.all()
        if device in supervisedDevices or user == device.owner:
            return device

        raise serializers.ValidationError(
                _("Container cannot be assigned to this device."),
                code="forbidden_action"
            )


class ContainerCreateOnlySerializer(ContainerSerializer):
    class Meta:
        model = Container
        fields = [
            "uuid",
            "capacity",
            "device",
            "position",
            "last_refil",
            "fill_status"
        ]
        read_only_fields = [
            "fill_status"
        ]
        validators = [
            # assert position uniqueness
            UniqueTogetherValidator(
                queryset=Container.objects.all(),
                fields=["position", "device"]
            )
        ]

    def create(self, validated_data):
        """
        Create already with chambers.
        """
        container = Container.objects.create_with_chambers(**validated_data)
        return container
