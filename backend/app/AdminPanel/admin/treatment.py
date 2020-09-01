"""
Admin page for treatment settings.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin
from ..models import Treatment

class TreatmentAdmin(admin.ModelAdmin):
    model = Treatment
    list_display = (
        "uuid",
        "name",
        "patient"
    )
    list_filter = (
        "name",
        "patient"
    )
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "patient", 
            )
        }),
    )
 