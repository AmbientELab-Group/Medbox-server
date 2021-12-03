
from django.contrib import admin
from API.models import DebugLog


class DebugLogAdmin(admin.ModelAdmin):
    model = DebugLog
    list_display = (
        "uuid",
        "device",
        "severity",
        "timestamp",
        "message_code",
        "details"
    )
    list_filter = (
        "device",
        "severity",
        "timestamp",
        "message_code",
    )
    fieldsets = (
        (None, {
            "fields": (
                "device",
                "severity",
                "timestamp",
                "message_code",
                "details"
            )
        }),
    )
