from django.contrib import admin
from ..models import Treatment


class TreatmentAdmin(admin.ModelAdmin):
    model = Treatment
    list_display = (
        "uuid",
        "name",
        "associated_user"
    )
    list_filter = (
        "name",
        "associated_user"
    )
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "associated_user",
            )
        }),
    )
