from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import ChamberSerializer
from DeviceAPI.models import Chamber


class ChamberList(generics.ListAPIView):
    queryset = Chamber.objects.all()
    serializer_class = ChamberSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        queryset = queryset.filter(owner=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ChamberDetail(generics.RetrieveAPIView):
    queryset = Chamber.objects.all()
    serializer_class = ChamberSerializer
    permission_classes = [IsAuthenticated]
