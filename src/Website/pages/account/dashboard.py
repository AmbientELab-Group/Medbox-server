from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login-page')
def dashboard(request):
    return render(request, 'web/account/dashboard.html', {})

