from rest_framework import serializers
from AdminPanel.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "email",
            "first_name",
            "last_name",
            "supervisedDevices"
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def save(self):
        user = User(
            email=self.validated_data["email"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})

        user.set_password(password)
        user.save()

        return user
