"""
Password change form.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "17.5.2020" 

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password

class PasswordChangeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = (kwargs.pop('user', None))
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        
    oldPassword = forms.CharField(label='Old password', widget=forms.PasswordInput())
    newPassword1 = forms.CharField(label='New password', widget=forms.PasswordInput())
    newPassword2 = forms.CharField(label='Repeat new password', widget=forms.PasswordInput())
    
    def clean(self):
        cleanedData = super().clean()
        oldPassword = cleanedData.get('oldPassword')
        newPassword1 = cleanedData.get('newPassword1')
        newPassword2 = cleanedData.get('newPassword2')
        
        # verify if passwords do match
        if newPassword1 != newPassword2:
            raise forms.ValidationError('Passwords do not match!')
        
        if (newPassword1 is None) or (newPassword2 is None):
            raise forms.ValidationError('Password field is empty!')
        
        # check if password meet's all criteria
        validate_password(newPassword1, self.user)
        
        validate_password
        # check if user's password is valid
        if not self.user.check_password(oldPassword):
            raise forms.ValidationError('Old password is not correct!')

@login_required(login_url='login-page')
def passwdChange(request):
    if request.method == 'POST':
        # populate form from POST request and add user to the object so validator can check old password
        # old password is checked in clean method because otherwise the error would have to be signalized in a different way
        form = PasswordChangeForm(request.POST, user=request.user)
        if form.is_valid():
            request.user.set_password(form.cleaned_data.get('newPassword1'))
            request.user.save()

            # logout user, he will be then redirected to the login page
            messages.success(request, 'Password changed succesfully! Please login!')
            return redirect('logout-page')
    
    else:
        form = PasswordChangeForm(request.POST, user=request.user)
    
    return render(request, 'web/account/passwordChange.html', {'form': form})
