"""
All models.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin

from .user import UserAdmin
from ..models import User

# register admin site
admin.site.register(User, UserAdmin)
