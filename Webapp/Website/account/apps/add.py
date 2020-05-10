from django.http import HttpResponse

def add(request):
    return HttpResponse('<h1>Account app addition page </h1>') 
