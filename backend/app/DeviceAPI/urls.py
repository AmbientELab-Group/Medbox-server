from django.urls import path
from DeviceAPI.views import (
    DeviceList,
    DeviceDetail,
    ContainerListCreateView,
    ContainerDetailView,
    PairingInfoCreate,
    PairingConfirm,
    PairingVerify,
    TelemetryLogView,
    PairingCodeCheck,
    TelemetryLogView,
    DebugLogView,
    ListDeviceVersions,
    ListContainerVersions,
)

urlpatterns = [
    path("devices", DeviceList.as_view()),
    path("devices/<uuid:pk>", DeviceDetail.as_view()),
    path("containers", ContainerListCreateView.as_view()),
    path("containers/<uuid:pk>", ContainerDetailView.as_view()),
    path("pairing/", PairingInfoCreate.as_view()),
    path("devices/pairing/confirm/", PairingConfirm.as_view()),
    path("pairing/verify/<pk>", PairingVerify.as_view()),
    path("telemetry", TelemetryLogView.as_view()),
    path("pairing/checkPairingCode",PairingCodeCheck.as_view()),
    path("debug/logs", DebugLogView.as_view()),
    path("versions/device", ListDeviceVersions.as_view()),
    path("versions/container", ListContainerVersions.as_view()),
]
