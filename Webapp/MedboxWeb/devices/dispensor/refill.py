from django.http import HttpResponse

def refill(request):
    return HttpResponse('<h1> Device refill page page </h1>') 
