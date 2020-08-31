"""
Admin page for device settings.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin
from ..models import Device

class DeviceAdmin(admin.ModelAdmin):
    model = Device
    list_display = (
        "uuid",
        "name",
        "pairingKey",
        "pairingKeyExpiresAt",
        "apiToken",
    )
    list_filter = (
        "name",
    )
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "users",
                "containers"
            )
        }),
    )
 