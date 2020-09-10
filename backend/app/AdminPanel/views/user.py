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

# working example of restricted endpoint, to remove later
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)


@api_view(["POST"])
def sign_up_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    status_code = None
    if serializer.is_valid():
        user = serializer.save()
        data["response"] = "Successfully registered a new user."
        data["email"] = user.email
        data["first_name"] = user.first_name
        data["last_name"] = user.last_name
        refresh = RefreshToken.for_user(user)
        data["refresh_token"] = str(refresh)
        data["access_token"] = str(refresh.access_token)
    else:
        data = serializer.errors
        status_code = status.HTTP_400_BAD_REQUEST

    return Response(data, status_code)
