from django.contrib import admin
from ..models import Device


class DeviceAdmin(admin.ModelAdmin):
    model = Device
    list_display = (
        "uuid",
        "name",
        "capacity",
        "owner",
        "pairing_key",
        "pairing_key_expires_at",
        "api_token",
    )
    list_filter = (
        "name",
        "capacity",
        "owner"
    )
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "capacity",
                "owner"
            )
        }),
    )
