"""
Admin page for predefinedTime settings.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin
from ..models import PredefinedTime

class PredefinedTimeAdmin(admin.ModelAdmin):
    model = PredefinedTime
    list_display = (
        "uuid",
        "name",
        "time",
        "owner"
    )
    list_filter = (
        "name",
        "time"
    )
    fieldsets = (
        (None, {
            "fields": (
                "name", 
                "time",
                "owner"
            )
        }),
    )
 