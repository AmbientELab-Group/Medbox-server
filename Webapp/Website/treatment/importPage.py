from django.http import HttpResponse

def importPage(request):
    return HttpResponse('<h1>Treatment import page </h1>')  
