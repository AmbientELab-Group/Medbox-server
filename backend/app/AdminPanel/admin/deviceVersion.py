"""
Admin page for device version settings.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin
from ..models import DeviceVersion

class DeviceVersionAdmin(admin.ModelAdmin):
    model = DeviceVersion
    list_display = (
        "uuid",
        "name",
        "capacity"
    )
    list_filter = (
        "name",
        "capacity"
    )
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "capacity"
            )
        }),
    )
 