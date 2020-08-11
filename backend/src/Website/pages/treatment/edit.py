"""
Treatment edit page.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "21.5.2020" 

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from Website.models import Treatment

class TreatmentSettings(forms.ModelForm):
    """
    General settings of the treatment.
    """
    class Meta:
        model = Treatment
        fields = ['patientFirstName', 'patientLastName']

@login_required(login_url='login-page')
def edit(request, treatmentID):
    # check if treatment ID is a valid string
    if (not (treatmentID.isdigit())) and treatmentID != 'new':
        messages.error(request, 'Invalid treatment ID')
        return redirect('treatment-dashboard')
     
    # if we are adding new treatment then add an empty object with empty name and surname and
    # redirect to it's database
    if treatmentID == 'new':
        newTreatment = Treatment(patientFirstName="", patientLastName="")
        newTreatment.save()
        return redirect('treatment-edit', treatmentID=newTreatment.id)

    # acquire treatment object instance
    try:
        treatmentInstance = Treatment.objects.get(id=int(treatmentID))
    except ObjectDoesNotExist:
        messages.error(request, 'Invalid treatment ID')
        return redirect('treatment-dashboard')
    
    if request.method == 'POST':
        form = TreatmentSettings(request.POST, instance=treatmentInstance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Treatment updated succesfully!')
            return redirect('treatment-edit', treatmentID=treatmentID)
    else:
        form = TreatmentSettings(instance=treatmentInstance)
            
    return render(request, 'web/treatment/edit.html', {'form': form,
                    'medicines': treatmentInstance.medicines.all(),
                    'treatmentID': treatmentID})
