from django.urls import path
from DeviceAPI.views import (
    DeviceList,
    DeviceDetail,
    ContainerListCreateView,
    ContainerDetailView,
    DevicePairing
)

urlpatterns = [
    path("devices", DeviceList.as_view()),
    path("devices/<uuid:pk>", DeviceDetail.as_view()),
    path("containers", ContainerListCreateView.as_view()),
    path("containers/<uuid:pk>", ContainerDetailView.as_view()),
    path("pairing/", DevicePairing.as_view())
]
