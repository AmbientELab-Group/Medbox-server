from .treatments import TreatmentsListCreateView, TreatmentsDetailView
from .medicines import MedicineListCreateView, MedicineDetailView
from .device import DeviceList, DeviceDetail, PairingConfirm
from .container import ContainerListCreateView, ContainerDetailView
from .telemetryLog import TelemetryLogView
from .devicePairing import PairingVerify, PairingInfoCreate, PairingCodeCheck
from .debugLog import DebugLogView
from .version import ListDeviceVersions, ListContainerVersions
from .chamber import ChamberList, ChamberDetail
from .dose import DoseDetailView, DoseListCreateView
