__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "1.5.2020"

from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    # admin panel site
    path("admin/", admin.site.urls),

    path("api/", get_schema_view(
        title="MedBox API",
        description="Schema of all the endpoints",
        version="1.0.0",
        public=True
    ), name="openapi-schema"),

    # account related api
    # (signin, signup, users, tokens)
    path("api/account/", include("AdminPanel.urls")),

    # application related api
    # (treatments, doses, medicines)
    path("api/", include("AppAPI.urls")),

    # device related api
    # (devices, containers, chambers, versions, internal device api)
    path("api/", include("DeviceAPI.urls")),
]
