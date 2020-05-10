from django.shortcuts import render

def register(request):
    return render(request, 'web/auth/register.html', {})
