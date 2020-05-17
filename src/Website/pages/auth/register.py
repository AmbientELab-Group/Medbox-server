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

class RegistrationForm(forms.ModelForm):
    """
    Form used for registration.
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
    
    # add additional fields for passwords
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())
    
    def clean(self):
        cleanedData = super().clean()
        password1 = cleanedData.get('password1')
        password2 = cleanedData.get('password2')
        
        # verify if passwords do match
        if password1 != password2:
             raise forms.ValidationError('Passwords do not match!')
            
def register(request):
    if request.method == 'POST':
        # populate a form from a request
        form = RegistrationForm(request.POST)
        
        # if form is valid then register new user and redirect to the login page
        if form.is_valid():
            newUser = form.save(commit=False)
            newUser.set_password(form.cleaned_data.get('password1'))
            newUser.save()
            form.save_m2m()
            
            # redirect to login page
            messages.success(request, 'Registration successfull! Now please login.')
            return redirect('login-page')
    
    else:
        form = RegistrationForm(request.POST)

    return render(request, 'web/auth/register.html', {'form': form})
