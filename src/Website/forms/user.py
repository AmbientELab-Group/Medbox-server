"""
Forms necessary for user administration to work.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

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
