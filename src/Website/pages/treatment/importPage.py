"""
View for importing treatment by token.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "24.5.2020"

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from Website.models import TreatmentToken
from django.contrib import messages

class TokenForm(forms.Form):
    """
    Token entering form.
    """
    tokenPart1 = forms.CharField(max_length=4, min_length=4)
    tokenPart2 = forms.CharField(max_length=4, min_length=4)
    tokenPart3 = forms.CharField(max_length=4, min_length=4)
    tokenPart4 = forms.CharField(max_length=4, min_length=4)

@login_required(login_url='login-page')
def importPage(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            tokenStr =  form.cleaned_data.get('tokenPart1')
            tokenStr += form.cleaned_data.get('tokenPart2')
            tokenStr += form.cleaned_data.get('tokenPart3')
            tokenStr += form.cleaned_data.get('tokenPart4')
            
            # try to find the token
            tokens = TreatmentToken.objects.filter(token__exact=tokenStr)
            if tokens.count() == 0:
                messages.error(request, 'Invalid token!')
                return redirect('treatment-import')
            
            # token is valid, add current account to he treatment if it is not already added
            treatment = tokens[0].treatment
            treatment.caretaker = request.user
            treatment.save()
            
            # delete used token from the database
            tokens[0].delete()
            
            # redirect to treatment dashboard
            messages.success(request, 'Treatment imported succesfully!')
            return redirect('treatment-dashboard')
            
    # start from the empty from every time
    form = TokenForm()
    return render(request, 'web/treatment/import.html', {'form': form})
