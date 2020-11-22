import binascii
import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class DeviceToken(models.Model):
    """
    Custom authorization token based on rest framework token
    """
    key = models.CharField(
        _("Key"),
        max_length=40,
        primary_key=True
    )

    # The name of this field has to stay the same for compatibility sake.
    # Now the "user" is a device that this token authenticates.
    user = models.OneToOneField(
        "Device",
        related_name='api_token',
        on_delete=models.CASCADE, 
        verbose_name=_("Device")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
        verbose_name = _("DeviceToken")
        verbose_name_plural = _("DeviceTokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(16)).decode()

    def __str__(self):
        return self.key

# NOT SURE IF THAT IS NEEDED, WILL LEAVE IT HERE FOR NOW TILL TESTING IS DONE
# class TokenProxy(Token):
#     """
#     Proxy mapping pk to user pk for use in admin.
#     """
#     @property
#     def pk(self):
#         return self.user.pk

#     class Meta:
#         proxy = 'rest_framework.authtoken' in settings.INSTALLED_APPS
#         abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
#         verbose_name = "token"
