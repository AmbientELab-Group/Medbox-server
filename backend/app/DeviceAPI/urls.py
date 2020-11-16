"""
Medbox device API URL routing config.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "25.5.2020"

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from DeviceAPI.views import (
    DeviceList,
    DeviceDetail,
    ContainerListCreateView,
    ContainerDetailView
)

urlpatterns = [
    path("devices", DeviceList.as_view()),
    path("devices/<uuid:pk>", DeviceDetail.as_view()),
    path("containers", ContainerListCreateView.as_view()),
    path("containers/<uuid:pk>", ContainerDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
