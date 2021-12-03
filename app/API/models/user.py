__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020"

from django.db import models
from django.contrib.auth.models import AbstractUser
from API.managers import UserManager
import uuid as UUID


class User(AbstractUser):
    # universal identifier
    uuid = models.UUIDField(
        primary_key=True,
        default=UUID.uuid4,
        editable=False,
        unique=True
    )

    # remove username field
    username = None
    first_name = None
    last_login = None

    # make email required
    email = models.EmailField("email address", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
