"""
View for deleting medicine.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "23.5.2020" 

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from Website.models import Treatment, Medicine, MedicineDosing, AdherenceTime

@login_required(login_url='login-page')
def delete(request, treatmentID, medicineID):
    # verify if treatment ID is a digit
    if not (treatmentID.isdigit()):
        messages.error(request, 'Invalid treatment ID!')
        return redirect('treatment-dashboard')

    # try to load treatment instance to see if it exists
    try:
        treatmentInstance = Treatment.objects.get(id=int(treatmentID))
    except ObjectDoesNotExist:
        messages.error(request, 'Invalid treatment ID!')
        return redirect('treatment-dashboard')
    
    # verify if medicine ID is a digit
    if not (medicineID.isdigit()):
        messages.error(request, 'Invalid medicine ID!')
        return redirect('treatment-edit', treatmentID=treatmentID)
    
    # simply find the medicineDosing object that has the given ID and delete it
    try:
        medicineDosing = MedicineDosing.objects.get(id=int(medicineID))
        medicineDosing.delete()
    except ObjectDoesNotExist:
        messages.error(request, 'Error occured while quering database!')
        return redirect('treatment-edit', treatmentID=treatmentID)
    
    messages.info(request, 'Medicine deleted succesfully!')
    return redirect('treatment-edit', treatmentID=treatmentID)
    
