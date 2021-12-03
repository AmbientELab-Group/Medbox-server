
from django.contrib import admin
from API.models import Chamber


class ChamberAdmin(admin.ModelAdmin):
    model = Chamber
    list_display = (
        "uuid",
        "container",
        "position",
        "is_full",
        "real_administration_time"
    )
    list_filter = (
        "position",
        "is_full",
        "real_administration_time"
    )
    fieldsets = (
        (None, {
            "fields": (
                "container",
                "position",
                "is_full",
            )
        }),
    )
