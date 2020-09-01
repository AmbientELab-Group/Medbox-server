"""
Admin page for container settings.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin
from ..models import Container

class ContainerAdmin(admin.ModelAdmin):
    model = Container
    list_display = (
        "uuid",
        "device",
        "position",
        "lastRefill"
    )
    list_filter = (
        "device",
        "version",
        "position",
        "lastRefill"
    )
    fieldsets = (
        (None, {
            "fields": (
                "version",
                "device",
                "position",
                "lastRefill",
            )
        }),
    )
 