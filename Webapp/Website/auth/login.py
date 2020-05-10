from django.http import HttpResponse

def login(request):
    return HttpResponse('<h1> Login page </h1>')
