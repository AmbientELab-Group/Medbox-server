"""
View for adding new medicine.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "23.5.2020"

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from Website.models import Treatment, Medicine, MedicineDosing, AdherenceTime
from .form import MedicineForm

@login_required(login_url='login-page')
def add(request, treatmentID):
    # verify if treatment ID is a digit
    if not (treatmentID.isdigit()):
        messages.error(request, 'Invalid treatment ID!')
        return redirect('treatment-dashboard')
    
    # get treatment instance, this is here in case some shit happens to url
    # then we don't want user to fill the form only to find out that he cannot post it
    try:
        treatmentInstance = Treatment.objects.get(id=int(treatmentID))
    except ObjectDoesNotExist:
        messages.error(request, 'Invalid treatment ID!')
        return redirect('treatment-dashboard')
    
    # process form data
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            # create new medicine object
            medicine = Medicine(name=form.cleaned_data.get('name'))
            medicine.save()
            
            # create new time object
            adherenceTime = AdherenceTime(time=form.cleaned_data.get('timeOfTaking'))
            adherenceTime.save()
            
            # create new medicine dosing object
            medicineDosing = MedicineDosing(medicine=medicine,
                                            doses=[form.cleaned_data.get('dose')],
                                            emergency=form.cleaned_data.get('emergency'),
                                            takenFrom=form.cleaned_data.get('takenFrom'),
                                            takenTo=form.cleaned_data.get('takenTo'))
            medicineDosing.save()
            medicineDosing.adherenceTimes.add(adherenceTime)
            medicineDosing.save()
                                            
            # add medicine dosing to the treatment instance
            treatmentInstance.medicines.add(medicineDosing)
            treatmentInstance.save()
            
            # redirect to the treatment edit page
            messages.success(request, 'Medicine added succesfully!')
            return redirect('treatment-edit', treatmentID=treatmentID)
    else:
        form = MedicineForm()
    
    return render(request, 'web/treatment/medicine.html', {'form': form})
