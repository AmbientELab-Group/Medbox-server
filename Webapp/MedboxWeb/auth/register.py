from django.http import HttpResponse

def register(request):
    return HttpResponse('<h1> Registration page </h1>')
