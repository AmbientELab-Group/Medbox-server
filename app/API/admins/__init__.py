from django.contrib import admin

from .medicine import MedicineAdmin
from .dose import DoseAdmin
from .treatment import TreatmentAdmin
from .predefinedTime import PredefinedTimeAdmin
from .chamber import ChamberAdmin
from .container import ContainerAdmin
from .device import DeviceAdmin
from .debugLog import DebugLogAdmin
from .telemetryLog import TelemetryLogAdmin
from .deviceToken import DeviceTokenAdmin
from .deviceVersion import DeviceVersionAdmin
from .containerVersion import ContainerVersionAdmin
from .pairingInfo import PairingInfoAdmin

from .user import UserAdmin
from API.models import (
    Treatment,
    Dose,
    Medicine,
    PredefinedTime,
    User,
    Device,
    Container,
    Chamber,
    DebugLog,
    TelemetryLog,
    DeviceToken,
    DeviceVersion,
    ContainerVersion,
    PairingInfo
)

admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Dose, DoseAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(PredefinedTime, PredefinedTimeAdmin)
admin.site.register(User, UserAdmin)

admin.site.register(Device, DeviceAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Chamber, ChamberAdmin)
admin.site.register(DebugLog, DebugLogAdmin)
admin.site.register(TelemetryLog, TelemetryLogAdmin)
admin.site.register(DeviceToken, DeviceTokenAdmin)
admin.site.register(DeviceVersion, DeviceVersionAdmin)
admin.site.register(ContainerVersion, ContainerVersionAdmin)
admin.site.register(PairingInfo, PairingInfoAdmin)
