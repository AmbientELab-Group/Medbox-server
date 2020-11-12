from django.shortcuts import render

def add(request):
    return render(request, 'web/account/apps/add.html', {})
