__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "10.5.2020"

from django.urls import path
from AdminPanel.views import user as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/<uuid:pk>", UserViews.user_info),
    path("signup", UserViews.sign_up_view),
    path("signin", TokenObtainPairView.as_view())
]
