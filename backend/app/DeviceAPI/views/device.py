from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import DeviceSerializer
from DeviceAPI.models import Device
from AdminPanel.serializers.user import UserSerializer


class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        user = request.user
        self.request.data["owner"] = str(user.uuid)
        serializer = self.serializer_class(data=self.request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        print(serializer.errors)
        serializer.save()

        return Response(self.request.data)


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]
