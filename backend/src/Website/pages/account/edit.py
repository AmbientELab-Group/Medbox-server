"""
User account update page.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "17.5.2020" 

from django.shortcuts import render, redirect
from django.contrib import messages
from Website.models import User
from django import forms
from django.contrib.auth.decorators import login_required

class UserEditForm(forms.ModelForm):
    """
    Form for editing already registered users.
    """
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
            
    
@login_required(login_url='login-page')
def edit(request):
    if request.method == 'POST':
        # populate from the request
        form = UserEditForm(request.POST, instance=request.user)
        
        # if form is valid update current user and redirect to the user dashboard with a success message
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile succesfully updated!')
            return redirect('user-dashboard')
    else:
        # populate form from the current user
        form = UserEditForm(instance=request.user)
        
    return render(request, 'web/account/edit.html', {'form': form})
