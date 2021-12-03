#from backend.app.AppAPI.views.medecines import MedecineDetailView, MedecineListCreateView
from django.urls import path
from API.views import (
    TreatmentsListCreateView,
    TreatmentsDetailView,
    MedicineListCreateView,
    MedicineDetailView,
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
    ChamberList,
    ChamberDetail,
    DoseListCreateView,
    DoseDetailView,
)

urlpatterns = [
    path("treatments/", TreatmentsListCreateView.as_view()),
    path("treatments/<pk>", TreatmentsDetailView.as_view()),
    path("medicines/", MedicineListCreateView.as_view()),
    path("medicines/<pk>", MedicineDetailView.as_view()),
    path("devices", DeviceList.as_view()),
    path("devices/<uuid:pk>", DeviceDetail.as_view()),
    path("containers", ContainerListCreateView.as_view()),
    path("containers/<uuid:pk>", ContainerDetailView.as_view()),
    path("pairing/", PairingInfoCreate.as_view()),
    path("devices/pairing/confirm/", PairingConfirm.as_view()),
    path("pairing/verify/<pk>", PairingVerify.as_view()),
    path("telemetry", TelemetryLogView.as_view()),
    path("pairing/checkPairingCode", PairingCodeCheck.as_view()),
    path("debug/logs", DebugLogView.as_view()),
    path("versions/device", ListDeviceVersions.as_view()),
    path("versions/container", ListContainerVersions.as_view()),
    path("chambers", ChamberList.as_view()),
    path("chambers/<uuid:pk>", ChamberDetail.as_view()),
    path("doses/", DoseListCreateView.as_view()),
    path("doses/<uuid:pk>", DoseDetailView.as_view())
]
 