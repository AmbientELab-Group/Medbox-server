from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.authentication import DeviceTokenAuthentication
from DeviceAPI.serializers import TelemetrySerializer


class TelemetryLogView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = TelemetrySerializer(data=request.data)
        token = DeviceTokenAuthentication.model.objects.get()
        device_id = str(token.user).split(':')[1]
        if serializer.is_valid():
            serializer.save(device_id=device_id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
