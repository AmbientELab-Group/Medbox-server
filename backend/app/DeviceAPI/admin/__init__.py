from django.contrib import admin
from .chamber import ChamberAdmin
from .container import ContainerAdmin
from .device import DeviceAdmin
from .debugLog import DebugLogAdmin
from .telemetryLog import TelemetryLogAdmin
from .deviceToken import DeviceTokenAdmin
from .deviceVersion import DeviceVersionAdmin
from .containerVersion import ContainerVersionAdmin
from .pairingInfo import PairingInfoAdmin

from ..models import (
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

admin.site.register(Device, DeviceAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Chamber, ChamberAdmin)
admin.site.register(DebugLog, DebugLogAdmin)
admin.site.register(TelemetryLog, TelemetryLogAdmin)
admin.site.register(DeviceToken, DeviceTokenAdmin)
admin.site.register(DeviceVersion, DeviceVersionAdmin)
admin.site.register(ContainerVersion, ContainerVersionAdmin)
admin.site.register(PairingInfo, PairingInfoAdmin)
