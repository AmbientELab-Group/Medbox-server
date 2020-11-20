from django.contrib import admin
from ..models import ContainerVersion


class ContainerVersionAdmin(admin.ModelAdmin):
    model = ContainerVersion
    list_display = (
        "name",
        "capacity",
    )
    list_filter = (
        "name",
        "capacity"
    )
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "capacity",
            )
        }),
    )
