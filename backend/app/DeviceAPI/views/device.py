from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import DeviceSerializer
from DeviceAPI.models import Device
from DeviceAPI.serializers import PairingInfoSerializer


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


class DevicePairing(APIView):
    """Endpoint for pairing device."""
    queryset = Device.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PairingInfoSerializer(data = request.data, many = False)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
