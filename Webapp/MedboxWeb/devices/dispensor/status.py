from django.http import HttpResponse

def status(request):
    return HttpResponse('<h1> Device status page </h1>') 
