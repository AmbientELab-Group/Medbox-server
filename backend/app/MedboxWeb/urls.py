__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "1.5.2020"

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # admin panel site
    path("admin/", admin.site.urls),

    # account related api
    path("api/account/", include("AdminPanel.urls")),

    # main api
    path("api/app/", include("AppAPI.urls")),

    # device related api
    path("api/device/", include("DeviceAPI.urls")),

    # JWT api
    path("api/token/refresh", TokenRefreshView.as_view()),
    path("api/token/verify", TokenVerifyView.as_view()),
]
