"""
View for deleting a device.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "26.5.2020"

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from DeviceAPI.models import Device
from Website.models import User

@login_required(login_url='login-page')
def delete(request, dispensorID):
    # doctors don't have access
    if request.user.role == User.Role.DOCTOR:
        messages.error(request, "You don't have permissions to access this site!")
        return redirect('user-dashboard')

    # try to find the device
    try:
        device = Device.objects.get(serialNumber=dispensorID)
        device.users.remove(request.user)
        device.save()
    except ObjectDoesNotExist:
        messages.error(request, 'Error occured while quering database!')
        return redirect('devices-dispensor-dashboard')
    
    messages.info(request, 'Device deleted succesfully!')
    return redirect('devices-dispensor-dashboard')
