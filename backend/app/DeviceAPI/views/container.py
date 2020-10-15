from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import ContainerSerializer
from DeviceAPI.models import Container, Device
from django.db.models import Q


class ContainerList(generics.ListCreateAPIView):
    """
    GET\n
    / - list all container associated with authorized user (owner/supervisor)\n
    ?device=\<UUID\> - all containers in the device passed as parameter\n
    POST\n
    / - creates container and related chambers to match capacity\n
    Data:
        (R) capacity - Num
        (R) device - UUID
        (O) position - Num
        (O) lastRefill - DateTime
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
        if position is None:
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
    GET\n
    / - retrive container associated with authorized user (owner/supervisor)\n
    PUT\n
    / - update container\n
    Data:
        (R) capacity - Num
        (R) position - Num
        (R) device - UUID
        (O) lastRefill - DateTime
    PATCH\n
    / - partial update container\n
    Data:
        (O) capacity - Num
        (O) position - Num
        (O) device - UUID
        (O) lastRefill - DateTime
    DELETE\n
    / - delete container
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

    # update containers positions when deleting middle one
    def perform_destroy(self, instance):
        affectedContainers = Container.objects.filter(
            Q(device=instance.device) &
            Q(position__gt=instance.position)
        )
        for container in affectedContainers:
            container.position -= 1
            container.save()
        instance.delete()
