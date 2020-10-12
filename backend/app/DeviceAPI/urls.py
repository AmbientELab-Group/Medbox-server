"""
Medbox device API URL routing config.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "25.5.2020"

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from DeviceAPI import views as DeviceViews
#from . import api


urlpatterns = [
    # API for requesting a token and key from the device
    #path("pairing/requestPairingKey", api.pairing.RequestKeys.as_view(),
    #     name="request-pairing-key"),
    path("devices", DeviceViews.DeviceList.as_view()),
    path("devices/<uuid:pk>", DeviceViews.DeviceDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
