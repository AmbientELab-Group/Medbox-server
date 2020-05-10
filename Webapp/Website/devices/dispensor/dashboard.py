from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('<h1> Device dashboard page </h1>') 
