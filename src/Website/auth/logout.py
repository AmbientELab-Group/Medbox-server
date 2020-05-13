"""
Logout handling.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "13.5.2020" 

from django.shortcuts import redirect
from django.contrib.auth import logout as logout_auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='login-page')
def logout(request):
    logout_auth(request)
    return redirect('login-page')
