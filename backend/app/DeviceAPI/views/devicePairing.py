from DeviceAPI.serializers import PairingInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from DeviceAPI.models import Device, PairingInfo
from rest_framework import status
from rest_framework.authtoken.models import Token

class PairingInfoCreate(APIView):
    """Endpoint for creating PairingInfo object"""

    def post(self, request):
        request.data["pairing_code"] = PairingInfo.generate_code()
        serializer = PairingInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pairing_info = serializer.save()
            return Response(data={"pairing_code": pairing_info.pairing_code})
        else:
            return Response(serializer.errors)


class PairingConfirmCode(APIView):
    """Endpoint for pairing by code"""

    def get(self, request, pk):
        try:
            pairing_info = PairingInfo.objects.get(pairing_code=pk)
        except PairingInfo.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        if pairing_info.is_expired():
            return Response(status=status.HTTP_403_FORBIDDEN)

        device = Device.objects.get(serial_number=pairing_info.serial_number)
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        data = {"token":token.key}
        return Response(data)

             
"""        try:
            code = user.PairingInfo.pairing_code
            if(code == pk)
                api_token = Token.objects.get(user = user)
                data = { "Token": api_token.key}
                return Response(data)
            else:
                return Response(status = status.HTTP_401_UNAUTHORIZED)
        except: 
            return Response(status = status.HTTP_403_FORBIDDEN) 
        try:
            code = user.PairingInfo.pairing_code
        except:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        else:
            if(code == pk):
                api_token = Token.objects.get(user = user)
                data = { "Token": api_token.key} """
        