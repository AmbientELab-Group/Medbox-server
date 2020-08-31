"""
Admin page for dose settings.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin
from ..models import Dose

class DoseAdmin(admin.ModelAdmin):
    model = Dose
    list_display = (
        "uuid",
        "medicine_name",
        "plannedAdministrationTime", 
        "numberOfPills",
        "onDemand",
        "chamber"
    )
    list_filter = (
        "plannedAdministrationTime", 
        "numberOfPills",
        "onDemand"
    )
    fieldsets = (
        (None, {
            "fields": (
                "plannedAdministrationTime", 
                "numberOfPills",
                "onDemand",
                "medicine",
                "chamber"
            )
        }),
    )

    def medicine_name(self, obj):
        return obj.medicine.name

 