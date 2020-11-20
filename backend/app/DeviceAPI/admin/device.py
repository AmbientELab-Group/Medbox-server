from django.contrib import admin
from ..models import Device


class DeviceAdmin(admin.ModelAdmin):
    model = Device
    list_display = (
        "uuid",
        "name",
        "version",
        "owner",
        "pairing_code",
        "pairing_code_expires_at",
        "api_token",
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
                "is_active"
            )
        }),
    )
