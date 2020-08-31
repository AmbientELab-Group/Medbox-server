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
        "position",
        "lastRefill"
    )
    list_filter = (
        "position",
        "lastRefill"
    )
    fieldsets = (
        (None, {
            "fields": (
                "position",
                "lastRefill",
                "chambers"
            )
        }),
    )
 