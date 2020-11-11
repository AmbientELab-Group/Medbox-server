from django.db import models
import uuid as UUID


class DebugLog(models.Model):
    class Severity(models.IntegerChoices):
        INFO = 0
        WARNING = 1
        CRITICAL = 2

    class MessageCode(models.IntegerChoices):
        DEVICE_ON = 0
        CONTAINER_IN = 1
        CONTAINER_OUT = 2
        BUTTON_PRESSED = 3

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

    # severity of the log
    severity = models.PositiveSmallIntegerField(
        choices=Severity.choices
    )

    # Unix time
    timestamp = models.PositiveIntegerField()

    # code of the message
    message_code = models.PositiveSmallIntegerField(
        choices=MessageCode.choices
    )

    # additional info about the log
    details = models.CharField(
        max_length=256,
        default="",
        blank=True
    )

    def __str__(self):
        return f"Code: {self.message_code} from {self.device} at {self.timestamp}"
