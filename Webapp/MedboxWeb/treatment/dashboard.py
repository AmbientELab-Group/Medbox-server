from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('<h1>Treatments dashboard page </h1>')  
