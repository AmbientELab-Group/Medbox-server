"""
Login page view.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "13.5.2020" 

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib import messages

def login(request):
    # if user is sending a form try to login
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login_auth(request, user)
            
            # redirect to home page
            return redirect('user-dashboard')

        else:
            messages.error(request, 'Invalid password or login.')
    
    # if user is logged in redirect him to the dashboard
    if request.user.is_authenticated:
        return redirect('user-dashboard')
    
    # otherwise just render a login page
    return render(request, 'web/auth/login.html', {})
