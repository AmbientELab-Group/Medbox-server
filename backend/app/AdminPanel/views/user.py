# from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from AdminPanel.models import User
from AdminPanel.serializers.user import (
    UserSerializer,
    RegistrationSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from AdminPanel.utils import Util
from django.contrib.sites.shortcuts import get_current_site


# endpoint for retriving personal information for authenticated user
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def user_info(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if request.user.uuid != pk:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializers = UserSerializer(user)
        return Response(serializers.data)


@api_view(["POST"])
def sign_up_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    status_code = None
    if serializer.is_valid():
        user = serializer.save()
        data["response"] = "Successfully registered a new user."
        refresh = RefreshToken.for_user(user)
        data["refresh_token"] = str(refresh)
        data["access_token"] = str(refresh.access_token)

        current_site = get_current_site(request).domain
        relative_link = 'email-verify/'

        email_token = RefreshToken.for_user(user).access_token
        abs_url = 'http://'+current_site+relative_link+"?token="+str(email_token)
        email_body = 'Hi '+user.first_name+' Use link bellow to verify your email \n'+abs_url

        email_data={
            'to_email': user.email,
            'email_body': email_body,
            'email_subject': 'Verify your email'
        }
    
        Util.send_email(email_data)

    else:
        data = serializer.errors
        status_code = status.HTTP_400_BAD_REQUEST


    return Response(data, status_code)

@api_view(["GET"])
def verify_email(request):
    pass
