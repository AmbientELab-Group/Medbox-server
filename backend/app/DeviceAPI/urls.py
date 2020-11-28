from django.urls import path
from DeviceAPI.views import (
    DeviceList,
    DeviceDetail,
    ContainerListCreateView,
    ContainerDetailView,
    PairingInfoCreate,
    PairingConfirm,
    PairingConfirmCode
)

urlpatterns = [
    path("devices", DeviceList.as_view()),
    path("devices/<uuid:pk>", DeviceDetail.as_view()),
    path("containers", ContainerListCreateView.as_view()),
    path("containers/<uuid:pk>", ContainerDetailView.as_view()),
    path("pairing/", PairingInfoCreate.as_view()),
    path("pairing/confirm/", PairingConfirm.as_view()),
    path("pairing/confirm/<uuid:pk>", PairingConfirmCode.as_view())
]
