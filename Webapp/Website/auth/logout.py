from django.shortcuts import redirect

def logout(request):
    redirect('auth/login')

