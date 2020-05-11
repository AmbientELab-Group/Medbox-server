from django.shortcuts import render

def add(request):
    return render(request, 'web/devices/dispensor/add.html', {})
