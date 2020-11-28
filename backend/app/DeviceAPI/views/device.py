from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import DeviceSerializer
from DeviceAPI.models import Device, deviceToken
from DeviceAPI.serializers import PairingInfoSerializer
from rest_framework.authtoken.models import Token


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


class PairingInfoCreate(APIView):
    """Endpoint for creating PairingInfo object"""
    queryset = Device.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PairingInfoSerializer(data = request.data, many = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PairingConfirm(APIView):
    """Endpoint for binding physical device to its db model"""
    queryset = Device.objects.all()
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        queryset = self.queryset
        user = self.request.user
        queryset = queryset.filter(user)

        #print(queryset.values())

        content = {
            "SerialNumber": SerialNumber
        }
        Device = queryset.filter(serial_number = SerialNumber)

        #print(queryset)

        #print(user)


        #device.serialnum = postedserialnum
        api_token = Token.objects.create(user = user)
        data = { "Token": api_token.key}
            
        return Response(data)


class PairingConfirmCode(APIView):
    """Endpoint for pairing by code"""
    queryset = Device.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        queryset = self.queryset
        user = self.request.user
        queryset = queryset.filter(pa)
             
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
        
#try:
#coś do zjebania
#except:
#coś co ma się wykonać gdy się zjebie
#else:
#coś co ma się wykonać gdy się nie zjebie