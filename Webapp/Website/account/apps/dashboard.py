from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('<h1>Account apps dashboard page </h1>') 
