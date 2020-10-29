from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import (
    ContainerSerializer,
    ContainerCreateOnlySerializer
)
from DeviceAPI.models import Container, Device
from django.db.models import Q


class ContainerList(generics.ListCreateAPIView):
    """
    Endpoint for managing containers.
    """
    serializer_class = ContainerCreateOnlySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        managedContainers = Container.objects.filter(
            Q(device__owner=user) |
            Q(device__in=user.supervisedDevices.all())
        )
        return managedContainers

    def list(self, request):
        containers = self.get_queryset()
        deviceUUID = request.query_params.get("device")
        serializer = self.get_serializer(containers, many=True)

        if deviceUUID is not None:
            requestedContainers = containers.filter(device__uuid=deviceUUID)

            if not requestedContainers:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(requestedContainers, many=True)

        return Response(serializer.data)

    # auto set first available position if position is missing
    # put container inbetween existing ones otherwise (modifies others)
    def create(self, request):
        containers = self.get_queryset()
        device = request.data.get("device")
        deviceObj = Device.objects.get(uuid=device)
        topContainer = containers.filter(device=device).order_by("-position").first()
        position = request.data.get("position")
        if position is None or topContainer is None:
            position = 0
            if topContainer is not None:
                position = topContainer.position + 1
        elif topContainer.position + 1 >= deviceObj.capacity:
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

        return Response(serializer.data)


class ContainerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint for managing containers.
    """
    serializer_class = ContainerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        managedContainers = Container.objects.filter(
            Q(device__owner=user) |
            Q(device__in=user.supervisedDevices.all())
        )
        return managedContainers

    # update affected containers positions
    def perform_update(self, serializer):
        queryset = self.get_queryset()
        oldPosition = self.get_object().position
        newPosition = serializer.validated_data.get("position")
        device = serializer.validated_data.get("device")
        if newPosition < oldPosition:
            affectedContainers = queryset.filter(
                Q(device=device) &
                Q(position__lt=oldPosition) &
                Q(position__gte=newPosition)
            )
            for container in affectedContainers:
                container.position += 1
                container.save()
        elif newPosition > oldPosition:
            affectedContainers = queryset.filter(
                Q(device=device) &
                Q(position__gt=oldPosition) &
                Q(position__lte=newPosition)
            )
            for container in affectedContainers:
                container.position -= 1
                container.save()

        serializer.save()

    # update containers positions when deleting middle one
    def perform_destroy(self, instance):
        queryset = self.get_queryset()
        affectedContainers = queryset.filter(
            Q(device=instance.device) &
            Q(position__gt=instance.position)
        )
        for container in affectedContainers:
            container.position -= 1
            container.save()
        instance.delete()