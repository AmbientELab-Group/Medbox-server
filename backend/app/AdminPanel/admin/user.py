"""
Code that makes edyting users throught admin page possible.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ..models import User

class UserCreationForm(UserCreationForm):
    """
    Form for creating a new user.
    """
    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'last_name')

class UserChangeForm(UserChangeForm):
    """
    Form for edyting an existing user.
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'first_name', 'last_name', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','first_name', 'last_name')
    ordering = ('email','first_name', 'last_name')
 
