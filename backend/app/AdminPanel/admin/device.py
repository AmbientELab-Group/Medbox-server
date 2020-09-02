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
        "version",
        "owner",
        "pairingKey",
        "pairingKeyExpiresAt",
        "apiToken",
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
                "owner"
            )
        }),
    )
 
