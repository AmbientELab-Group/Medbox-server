from django.db import models
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
import secrets


class PairingInfo(models.Model):
    # pairing key used to connect the device with a user's account
    pairing_code = models.PositiveIntegerField(
        primary_key=True
    )

    # creation date
    created_at = models.DateTimeField(auto_now_add=True)

    # factory serial number assigned to the device
    serial_number = models.UUIDField()

    # version of the hardware
    hardware_version = models.CharField(max_length=11)

    # version of the firmware
    firmware_version = models.CharField(max_length=11)

    @classmethod
    def generate_code(cls):
        code = secrets.randbelow(1000000)
        while cls.objects.filter(pairing_code=code).exists():
            code = secrets.randbelow(1000000)
        return code

    def expires_at(self):
        return self.created_at + timedelta(minutes=settings.PAIRING_CODE_LIFETIME)

    def is_expired(self):
        return self.expires_at() < timezone.now()

    def __str__(self):
        return f"{self.pairing_code}, created at: {self.created_at}"
