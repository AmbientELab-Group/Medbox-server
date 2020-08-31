"""
Admin page for chamber settings.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin
from ..models import Chamber

class ChamberAdmin(admin.ModelAdmin):
    model = Chamber
    list_display = (
        "uuid",
        "position",
        "isFull",
        "realAdministrationTime"
    )
    list_filter = (
        "position",
        "isFull",
        "realAdministrationTime"
    )
    fieldsets = (
        (None, {
            "fields": (
                "position",
                "isFull",
                "doses"
            )
        }),
    )
 