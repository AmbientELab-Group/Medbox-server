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
    # acquire treatment object instance
    treatmentInstance = None
    try:
        if treatmentID.isdigit():
            treatmentInstance = Treatment.objects.get(id=int(treatmentID))
        # there value is a string that is other than 'new' then just redirect to new
        elif treatmentID != 'new':
             redirect('treatment-edit', treatmentID='new')
    except ObjectDoesNotExist:
        messages.error(request, 'Invalid ID')
        redirect('treatment-edit', treatmentID='new')
    
    if request.method == 'POST':
        if treatmentInstance:
            form = TreatmentSettings(request.POST, instance=treatmentInstance)
        else:
            form = TreatmentSettings(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Treatment updated succesfully!')
            return redirect('treatment-edit', treatmentID=treatmentID)
    else:
        if treatmentID == 'new':
            form = TreatmentSettings()
        else:
            form = TreatmentSettings(instance=treatmentInstance)
            
        return render(request, 'web/treatment/edit.html', {'form': form})
