from django.contrib import admin
from API.models import Dose


class DoseAdmin(admin.ModelAdmin):
    model = Dose
    list_display = (
        "uuid",
        "medicine_name",
        "planned_administration_time",
        "number_of_pills",
        "on_demand",
        "chamber"
    )
    list_filter = (
        "planned_administration_time", 
        "number_of_pills",
        "on_demand"
    )
    fieldsets = (
        (None, {
            "fields": (
                "planned_administration_time",
                "number_of_pills",
                "on_demand",
                "medicine",
                "chamber",
                "treatment"
            )
        }),
    )

    def medicine_name(self, obj):
        return obj.medicine.name
