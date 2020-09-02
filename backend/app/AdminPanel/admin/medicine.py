__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin
from ..models import Medicine

class MedicineAdmin(admin.ModelAdmin):
    model = Medicine
    list_display = (
        "uuid", 
        "name", 
        "producer"
    )
    list_filter = (
        "name", 
        "producer"
    )
    fieldsets = (
        (None, {
            "fields": (
                "name", 
                "producer"
                )
        }),
    )

 
