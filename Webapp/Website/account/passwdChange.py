from django.http import HttpResponse

def passwdChange(request):
    return HttpResponse('<h1> Account password change </h1>')
