from django.contrib import admin
from API.models import Device


class DeviceAdmin(admin.ModelAdmin):
    model = Device
    list_display = (
        "uuid",
        "name",
        "version",
        "owner",
        "fill_status"
    )
    list_filter = (
        "name",
        "version",
        "owner"
    )
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "version",
                "owner",
                "supervisors",
                "is_active",
                "serial_number",
                "hardware_version",
                "firmware_version",
            )
        }),
    )
