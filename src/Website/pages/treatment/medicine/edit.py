"""
View for editing medicine.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "23.5.2020"

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from Website.models import Treatment, MedicineDosing
from .form import MedicineForm

@login_required(login_url='login-page')
def edit(request, treatmentID, medicineID):
    # verify if treatment ID is a digit
    if not (treatmentID.isdigit()):
        messages.error(request, 'Invalid treatment ID!')
        return redirect('treatment-dashboard')
    
    # try to get treatment instance
    try:
        treatmentInstance = Treatment.objects.get(id=int(treatmentID))
    except ObjectDoesNotExist:
        messages.error(request, 'Invalid treatment ID!')
        return redirect('treatment-dashboard')
    
    # verify if medicine ID is a digit
    if not (medicineID.isdigit()):
        messages.error(request, 'Invalid medicine ID!')
        return redirect('treatment-edit', treatmentID=treatmentID)
    
    # get medicine dosing object
    try:
        medicineDosing = MedicineDosing.objects.get(id=int(medicineID))
    except ObjectDoesNotExist:
        messages.error(request, 'Error occured while quering database!')
        # redirect to treatment edit page since we know that id is valid
        return redirect('treatment-edit', treatmentID=treatmentID)
    
    # TODO: Handle errors and revert to the previous state if error has occured
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            # save new medicine name
            medicineDosing.medicine.name = form.cleaned_data.get('name')
            medicineDosing.medicine.save()
            
            # save new medicine time
            medicineTime = medicineDosing.adherenceTimes.all()[0]
            medicineTime.time = form.cleaned_data.get('timeOfTaking')
            medicineTime.save()
            
            # save new treatment dosing parameters
            medicineDosing.emergency = form.cleaned_data.get('emergency')
            medicineDosing.doses[0] = form.cleaned_data.get('dose')
            medicineDosing.takenTo = form.cleaned_data.get('takenTo')
            medicineDosing.takenFrom = form.cleaned_data.get('takenFrom')
            medicineDosing.save()
            
            # redirect to medicine edit page
            messages.success(request, "Changes saved succesfully!")
            return redirect('treatment-edit', treatmentID=treatmentID)
            
    # initialize fields value from the medicine object
    else:
        form = MedicineForm()
        form.fields["name"].initial = medicineDosing.medicine.name
        form.fields["emergency"].initial = medicineDosing.emergency
        form.fields["dose"].initial = medicineDosing.doses[0]
        form.fields["timeOfTaking"].initial = medicineDosing.adherenceTimes.all()[0].time
        form.fields["takenTo"].initial = medicineDosing.takenTo
        form.fields["takenFrom"].initial = medicineDosing.takenFrom
        
    return render(request, 'web/treatment/medicine.html', {'form': form})
