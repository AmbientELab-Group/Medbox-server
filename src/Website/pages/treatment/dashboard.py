from django.shortcuts import render

def dashboard(request):
    return render(request, 'web/treatment/dashboard.html', {})