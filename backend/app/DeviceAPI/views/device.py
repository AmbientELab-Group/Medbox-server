from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import DeviceSerializer
from DeviceAPI.models import Device, PairingInfo



class DeviceList(generics.ListCreateAPIView):
    """Endpoint for managing devices."""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        queryset = queryset.filter(owner=request.user)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint for managing devices."""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


class PairingConfirm(APIView):
    """Endpoint for binding physical device to its db model"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        # get_or_404 todo
        try:
            device = Device.objects.get(pk=request.data.get("device_uuid"))
        except Device.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # this works, I've checked
        if not device.is_managed(user):
            return Response(status=status.HTTP_403_FORBIDDEN)

        # get or 404 todo
        try:
            info = PairingInfo.objects.get(pairing_code=request.data.get("pairing_code"))
        except PairingInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        device.serial_number = info.serial_number
        device.hardware_version = info.hardware_version
        device.firmware_version = info.firmware_version

        device.save()

        return Response(status=status.HTTP_201_CREATED)
