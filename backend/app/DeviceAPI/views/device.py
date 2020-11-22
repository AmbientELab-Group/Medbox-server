from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import DeviceSerializer
from DeviceAPI.models import Device
from DeviceAPI.serializers import PairingSerializer


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


class DevicePairing(generics.ListCreateAPIView):
    """Endpoint for pairing device."""
    queryset = Device.objects.all()
    #serializer_class = PairingGetSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        queryset = self.get_queryset()
        queryset = queryset.filter(uuid=pk).first()

        code = queryset.pairing_code
        #serializer = PairingGetSerializer(queryset, many=False)
        #return Response(serializer.data)
        
        return Response(data={"pairing_code": code})
    
    def post(self, request):
        pass
