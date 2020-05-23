"""
Treatment dashboard views.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "21.5.2020" 

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Website.models import User
from Website.models import Treatment
from django import forms
from django.contrib import messages

@login_required(login_url='login-page')
def dashboard(request):
    # render two different version of the page depending on whether it is seen by caretaker or doctor
    if request.user.role == User.Role.DOCTOR:
        return _dashboardDoctor(request)
    return _dashboardCaretaker(request)

@login_required(login_url='login-page')
def _dashboardCaretaker(request):
    # produce a list of treatments added to the caretakers account
    treatments = Treatment.objects.filter(caretaker__exact=request.user)
    return render(request, 'web/treatment/caretaker-dashboard.html', {'pairedTreatments': treatments})

class SearchForm(forms.Form):
    """
    Form used for searching.
    """
    firstName = forms.CharField(label='Patient First Name')
    lastName = forms.CharField(label='Patient Last Name')
    
@login_required(login_url='login-page')
def _dashboardDoctor(request):
    # process a search form
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # produce a list of found treatments
            treatments = Treatment.objects.filter(patientFirstName__exact=form.cleaned_data.get('firstName'),
                                                  patientLastName__exact=form.cleaned_data.get('lastName'))
            
            # tell user how many results found
            messages.info(request, '%d entries found!'%treatments.count())
            
            # return results of the search
            return render(request, 'web/treatment/doctor-dashboard.html', {'form': form, 'treatments': treatments})
    else:
        # create empty search form
        form = SearchForm()
    
    return render(request, 'web/treatment/doctor-dashboard.html', {'form': form, 'treatment': []})
