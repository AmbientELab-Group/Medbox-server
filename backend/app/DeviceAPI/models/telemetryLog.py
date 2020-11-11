from django.db import models
import uuid as UUID


class TelemetryLog(models.Model):
    class DeviceStatus(models.IntegerChoices):
        OK = 0
        UNEXPECTED_ERROR = 1
        BATTERY_LOW = 2

    # universal identifier
    uuid = models.UUIDField(
        primary_key=True,
        default=UUID.uuid4,
        editable=False,
        unique=True
    )

    # device this log came from
    device = models.ForeignKey(
        "Device",
        on_delete=models.CASCADE,
        related_name="debug_logs"
    )

    # Unix time
    timestamp = models.PositiveIntegerField()

    # Network connection strength
    signal_strength = models.PositiveSmallIntegerField()

    # A percent of battery left
    battery_status = models.PositiveSmallIntegerField()

    # Battery voltage
    battery_voltage = models.PositiveSmallIntegerField()

    # Status code of the device
    device_status = models.PositiveSmallIntegerField(
        choices=DeviceStatus.choices
    )

    def __str__(self):
        return f"Status: {self.device_status} from {self.device} at {self.timestamp}"
