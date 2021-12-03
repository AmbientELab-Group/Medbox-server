from django.contrib import admin
from API.models import DeviceVersion


class DeviceVersionAdmin(admin.ModelAdmin):
    model = DeviceVersion
    list_display = (
        "name",
        "capacity",
        "latest_firmware_version"
    )
    list_filter = (
        "name",
        "capacity"
    )
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "capacity",
                "latest_firmware_version"
            )
        }),
    )
