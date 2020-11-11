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
# from . import api


urlpatterns = [
    # API for requesting a token and key from the device
    # path("pairing/requestPairingKey", api.pairing.RequestKeys.as_view(),
    #     name="request-pairing-key"),
    path("devices", DeviceList.as_view()),
    path("devices/<uuid:pk>", DeviceDetail.as_view()),
    path("containers", ContainerListCreateView.as_view()),
    path("containers/<uuid:pk>", ContainerDetailView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
