from django.contrib import admin
from API.models import DeviceToken


class DeviceTokenAdmin(admin.ModelAdmin):
    model = DeviceToken
    list_display = (
        "key",
        "user",
        "created"
    )
    list_filter = (
        "user",
        "created"
    )
    fieldsets = (
        (None, {
            "fields": (
                "key",
                "user"
            )
        }),
    )
