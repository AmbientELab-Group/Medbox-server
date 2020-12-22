from rest_framework.views import APIView
from rest_framework.response import Response
from DeviceAPI.models import ContainerVersion, DeviceVersion
from DeviceAPI.serializers import ContainerVersionSerializer, DeviceVersionSerializer


class ListDeviceVersions(APIView):
    def get(self, request):
        deviceVersions = DeviceVersion.objects.all()
        serializer = DeviceVersionSerializer(deviceVersions, many=True)
        return Response(serializer.data)

class ListContainerVersions(APIView):
    def get(self, request):
        containerVersions = ContainerVersion.objects.all()
        serializer = ContainerVersionSerializer(containerVersions, many=True)
        return Response(serializer.data)