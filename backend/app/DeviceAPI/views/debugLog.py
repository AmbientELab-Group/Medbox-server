from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import DebugLogSerializer


class DebugLogView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DebugLogSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(device=request.user)
        return Response(status=status.HTTP_201_CREATED)
