"""
User registration page view.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "16.5.2020" 

from django.shortcuts import render, redirect
from django.contrib import messages
from Website.models import User
from django import forms
from django.contrib.auth import get_user_model

class RegistrationForm(forms.Form):
    """
    Form used for registration.
    """
    email = forms.EmailField(label='Email', max_length=100)
    firstName = forms.CharField(label='First name', max_length=1000)
    lastName = forms.CharField(label='Last name', max_length=1000)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())
    
    def clean(self):
        cleanedData = super().clean()
        password1 = cleanedData.get('password1')
        password2 = cleanedData.get('password2')
        
        if password1 != password2:
             raise forms.ValidationError('Passwords do not match!')

def register(request):
    if request.method == 'POST':
        # populate a form from a request
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            # verify if login has not been taken
            if User.objects.filter(email=form.cleaned_data.get('email')).exists():
                messages.error(request, 'Email already in use!')
                return render(request, 'web/auth/register.html', {'form': form})
            
            # register new user
            get_user_model().objects.create_user(
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password1'),
                first_name=form.cleaned_data.get('firstName'),
                last_name=form.cleaned_data.get('lastName'))
            
            # redirect to login page
            messages.success(request, 'Registration successfull! Now please login.')
            return redirect('user-dashboard')
    
    else:
        form = RegistrationForm(request.POST)

    return render(request, 'web/auth/register.html', {'form': form})
