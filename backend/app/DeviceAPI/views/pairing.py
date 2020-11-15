from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from ..models import DeviceToken, Device


class CreateDeviceToken(APIView):
    def post(self, request):
        device = request.data.get("device_uuid")
        if device is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        device_obj = Device.objects.get(pk=device)
        token = DeviceToken.objects.create(user=device_obj)

        return Response(data={"api_key": token.key})


class AuthenticatedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        return Response(data={"msg": "Wolololo"})
