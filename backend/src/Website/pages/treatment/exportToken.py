"""
View for generating new token for importing the treatment.
This view will just display a token on the screen.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "24.5.2020"

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Website.models import Treatment, TreatmentToken
from datetime import datetime,timedelta
from django.conf import settings
import secrets

@login_required(login_url='login-page')
def exportToken(request, treatmentID):
    # check if treatment ID is a valid string
    if (not (treatmentID.isdigit())) and treatmentID != 'new':
        messages.error(request, 'Invalid treatment ID')
        return redirect('treatment-dashboard')

    # acquire treatment object instance
    try:
        treatmentInstance = Treatment.objects.get(id=int(treatmentID))
    except ObjectDoesNotExist:
        messages.error(request, 'Invalid treatment ID')
        return redirect('treatment-dashboard')
    
    # if treatment already has an old token(s), remove it/them
    for token in TreatmentToken.objects.filter(treatment__exact=treatmentInstance).all():
        token.delete()
    
    # generate unique token
    while True:
        token = '{n:014d}'.format(n=secrets.randbelow(10**16))
        if TreatmentToken.objects.filter(token__exact=token).count() == 0:
            break

    treatmentToken = TreatmentToken(token=token,
                                    treatment=treatmentInstance,
                                    expires=datetime.now()+timedelta(hours=settings.TREATMENT_TOKEN_LIFETIME))
    treatmentToken.save()
    
    tokenStr = token[:4]+'-'+token[4:8]+'-'+token[8:12]+'-'+token[12:16]
    return render(request, 'web/treatment/exportToken.html', {'token':  tokenStr,
                                                              'treatmentID': treatmentID})
