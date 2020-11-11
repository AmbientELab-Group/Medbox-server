from django.contrib import admin
from .chamber import ChamberAdmin
from .container import ContainerAdmin
from .device import DeviceAdmin
from .debugLog import DebugLogAdmin
from .telemetryLog import TelemetryLogAdmin

from ..models import (
    Device,
    Container,
    Chamber,
    DebugLog,
    TelemetryLog
)

admin.site.register(Device, DeviceAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Chamber, ChamberAdmin)
admin.site.register(DebugLog, DebugLogAdmin)
admin.site.register(TelemetryLog, TelemetryLogAdmin)
