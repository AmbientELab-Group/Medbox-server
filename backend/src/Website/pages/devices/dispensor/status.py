from django.shortcuts import render

def status(request):
    return render(request, 'web/devices/dispensor/status.html', {})
