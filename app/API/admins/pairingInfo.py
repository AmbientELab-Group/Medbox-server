from django.contrib import admin
from API.models import PairingInfo


class PairingInfoAdmin(admin.ModelAdmin):
    model = PairingInfo
    list_display = (
        "pairing_code",
        "created_at",
        "serial_number",
        "hardware_version",
        "firmware_version",
        "is_expired"
    )
    list_filter = (
        "pairing_code",
        "created_at",
    )
    fieldsets = (
        (None, {
            "fields": (
                "pairing_code",
                "serial_number",
                "hardware_version",
                "firmware_version",
            )
        }),
    )
