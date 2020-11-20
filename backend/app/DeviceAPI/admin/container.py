from django.contrib import admin
from ..models import Container


class ContainerAdmin(admin.ModelAdmin):
    model = Container
    list_display = (
        "uuid",
        "device",
        "version",
        "position",
        "last_refill"
    )
    list_filter = (
        "device",
        "version",
        "position",
        "last_refill"
    )
    fieldsets = (
        (None, {
            "fields": (
                "version",
                "device",
                "position",
                "last_refill",
            )
        }),
    )
