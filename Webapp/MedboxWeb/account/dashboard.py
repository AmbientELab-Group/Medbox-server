from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('<h1>Account dashboard page </h1>')

