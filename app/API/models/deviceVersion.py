from django.db import models


class DeviceVersion(models.Model):
    # name of the version eg. 1.0
    name = models.CharField(
        primary_key=True,
        max_length=8
    )

    # max number of containers fitting to this version of device
    capacity = models.PositiveSmallIntegerField()

    # latest firmaware version this device should be updated to eg. 1.0.0
    latest_firmware_version = models.CharField(
        max_length=12
    )

    def __str__(self):
        return f"{self.name}"
