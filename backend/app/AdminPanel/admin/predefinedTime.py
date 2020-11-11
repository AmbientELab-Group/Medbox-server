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
