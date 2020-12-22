from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import (
    ContainerSerializer,
    ContainerCreateOnlySerializer
)
from DeviceAPI.models import Container, Device
from django.db.models import Q


class ContainerListCreateView(generics.ListCreateAPIView):
    """
    This is a view for listing collection of containers and creating new ones.
    """
    serializer_class = ContainerCreateOnlySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Allows to show only owned or managed containers.
        """
        user = self.request.user
        managed_containers = Container.objects.filter(
            Q(device__owner=user) |
            Q(device__in=user.supervised_devices.all())
        )
        return managed_containers

    def list(self, request):
        """
        This endpoint returns all owned or managed containers for authenticated
        user. May return only containers associated with a device specified in
        the request.
        """
        containers = self.get_queryset()
        device_UUID = request.query_params.get("device")
        serializer = self.get_serializer(containers, many=True)

        if device_UUID is not None:
            requested_containers = containers.filter(device__uuid=device_UUID)

            if not requested_containers:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(requested_containers, many=True)

        return Response(serializer.data)

    def create(self, request):
        """
        This endpoint allows to create new containers. If no position is
        explicitly specified for the new container, it is added on the first
        available position in a device specified in request. If position is
        specified in the range of already occupied positions the existing
        containers are modified to reflect the shift neccesary to insert the
        new container.
        """
        containers = self.get_queryset()
        device = request.data.get("device")
        device_obj = Device.objects.get(uuid=device)
        top_container = containers.filter(device=device).order_by("-position").first()
        position = request.data.get("position")
        if position is None or top_container is None:
            position = 0
            if top_container is not None:
                position = top_container.position + 1
        elif top_container.position + 1 >= device_obj.capacity:
            return Response(
                data={"detail": "Device is full"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            affectedContainers = containers.filter(position__gte=position)
            for container in affectedContainers:
                container.position += 1
                container.save()

        request.data["position"] = position
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContainerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This is a view for managing a single container. Contains retrive, update
    and destroy endpoints.
    """
    serializer_class = ContainerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Allows to show and modify only owned or managed containers.
        """
        user = self.request.user
        managed_containers = Container.objects.filter(
            Q(device__owner=user) |
            Q(device__in=user.supervised_devices.all())
        )
        return managed_containers

    def perform_update(self, serializer):
        """
        On every update, check end possibly correct positions of
        affected containers in the same device.
        """
        queryset = self.get_queryset()
        old_position = self.get_object().position
        old_device = self.get_object().device
        new_position = serializer.validated_data.get("position")
        new_device = serializer.validated_data.get("device")

        if old_device != new_device:
            if new_device.capacity <= queryset.filter(device=new_device).count():
                return Response(
                    data={"detail": "Device is full"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # container is removed from the old device
            affected_containers = queryset.filter(
                Q(device=old_device) &
                Q(position__gt=old_position)
            )
            for container in affected_containers:
                container.position -= 1
                container.save()

            # container is added to the new device
            affected_containers = queryset.filter(
                Q(device=new_device) &
                Q(position__gte=new_position)
            )
            for container in affected_containers:
                container.position += 1
                container.save()
        else:
            if new_position < old_position:
                # container is moved down
                affected_containers = queryset.filter(
                    Q(device=new_device) &
                    Q(position__lt=old_position) &
                    Q(position__gte=new_position)
                )
                for container in affected_containers:
                    container.position += 1
                    container.save()
            elif new_position > old_position:
                # container is moved up
                affected_containers = queryset.filter(
                    Q(device=new_device) &
                    Q(position__gt=old_position) &
                    Q(position__lte=new_position)
                )
                for container in affected_containers:
                    container.position -= 1
                    container.save()

        serializer.save()

    def perform_destroy(self, instance):
        """
        On every delete, check and possibly correct positions of
        affected containers in the same device.
        """
        queryset = self.get_queryset()
        affected_containers = queryset.filter(
            Q(device=instance.device) &
            Q(position__gt=instance.position)
        )
        for container in affected_containers:
            container.position -= 1
            container.save()
        instance.delete()
