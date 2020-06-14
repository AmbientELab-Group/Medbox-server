"""
Devices dashboard.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "26.5.2020" 

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from DeviceAPI.models import Device
from Website.models import User

@login_required(login_url='login-page')
def dashboard(request):
    # doctors don't have access
    if request.user.role == User.Role.DOCTOR:
        messages.error(request, "You don't have permissions to access this site!")
        return redirect('user-dashboard')
    
    # produce a list of all devices connected with the current account
    devices =  Device.objects.filter(users__exact=request.user)
    
    # list all devices connected with this account
    return render(request, 'web/devices/dispensor/dashboard.html', {'pairedDevices': devices.all()})
