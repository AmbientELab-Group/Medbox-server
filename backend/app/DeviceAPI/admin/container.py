from django.contrib import admin
from ..models import Container


class ContainerAdmin(admin.ModelAdmin):
    model = Container
    list_display = (
        "uuid",
        "device",
        "position",
        "last_refill"
    )
    list_filter = (
        "device",
        "capacity",
        "position",
        "last_refill"
    )
    fieldsets = (
        (None, {
            "fields": (
                "capacity",
                "device",
                "position",
                "last_refill",
            )
        }),
    )
