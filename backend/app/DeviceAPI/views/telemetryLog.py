from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import TelemetrySerializer


class TelemetryLogView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TelemetrySerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(device_id=request.user.uuid)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
