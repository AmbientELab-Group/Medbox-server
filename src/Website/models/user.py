"""
Model of the user.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.db import models
from django.contrib.auth.models import AbstractUser
from ..managers import UserManager

class User(AbstractUser):
    """
    User model.
    """

    # remove unnecessary fields
    username = None
    
    # make email required
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # add userID field
    userID = models.CharField(max_length=200)
    
    # user role
    class Role:
        DOCTOR = 'DR'
        CARETAKER = 'CRT'
    
    ROLE_CHOICES = [
        ('CRT', 'Caretaker'),
        ('DR', 'Doctor')
    ]
    
    role = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default='CRT',
    )

    # object manager
    objects = UserManager()
    
    def __str__(self):
        return self.email
