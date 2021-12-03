from django.urls import path
from API.views import user as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("users/<uuid:pk>", UserViews.user_info),
    path("signup", UserViews.sign_up_view),
    path("signin", TokenObtainPairView.as_view()),
    # JWT api
    path("token/refresh", TokenRefreshView.as_view()),
    path("token/verify", TokenVerifyView.as_view()),
]
