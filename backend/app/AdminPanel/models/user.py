"""
Model of the user.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.db import models
from django.contrib.auth.models import AbstractUser
from ..managers import UserManager
import uuid as UUID

# HELPER
# AbstractUser model has the following fields:
#     username
#     first_name
#     last_name
#     email
#     password
#     groups
#     user_permissions
#     is_staff
#     is_active
#     is_superuser
#     last_login
#     date_joined

class User(AbstractUser):
    """
    User model.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)
    
    # make email required
    email = models.EmailField("email address", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # object manager
    objects = UserManager()
    
    def __str__(self):
        return self.email
