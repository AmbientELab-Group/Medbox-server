"""
View for pairing a new device.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "26.5.2020"

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from DeviceAPI.models import Device
from AdminPanel.models import User

class CodeForm(forms.Form):
    """
    Form for entering code.
    """
    code = forms.CharField(max_length=6, min_length=6)
    name = forms.CharField(max_length=100)

@login_required(login_url='login-page')
def add(request):
    # doctors don't have access
    if request.user.role == User.Role.DOCTOR:
        messages.error(request, "You don't have permissions to access this site!")
        return redirect('user-dashboard')
    
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            
            # lookup the code
            keys = Device.objects.filter(pairingKey__exact=code)
            if keys.count() == 0:
                messages.error(request, 'Invalid code!')
                return redirect('devices-dispensor-add')
            
            # if the code exists then assign a current user to the current user
            key = keys[0]
            device = key.device
            device.users.add(request.user)
            device.name = form.cleaned_data.get('name')
            device.save()
            
            # also delete the code
            key.delete()
            
            messages.success(request, 'Device added succesfully!')
            return redirect('devices-dispensor-dashboard')
    
    form = CodeForm()
    return render(request, 'web/devices/dispensor/add.html', {'form': form})
