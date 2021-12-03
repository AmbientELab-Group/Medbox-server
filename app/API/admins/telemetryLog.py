from django.contrib import admin
from API.models import TelemetryLog


class TelemetryLogAdmin(admin.ModelAdmin):
    model = TelemetryLog
    list_display = (
        "uuid",
        "device",
        "timestamp",
        "device_status",
        "signal_strength",
        "battery_status",
        "battery_voltage",
    )
    list_filter = (
        "device",
        "timestamp",
        "device_status",
    )
    fieldsets = (
        (None, {
            "fields": (
                "device",
                "timestamp",
                "device_status",
                "signal_strength",
                "battery_status",
                "battery_voltage",
            )
        }),
    )
