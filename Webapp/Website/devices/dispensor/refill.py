from django.shortcuts import render

def refill(request):
    return render(request, 'web/devices/dispensor/refill.html', {})
