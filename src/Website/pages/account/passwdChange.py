from django.shortcuts import render

def passwdChange(request):
    return render(request, 'web/account/passwordChange.html', {})
