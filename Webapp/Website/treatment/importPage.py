from django.shortcuts import render

def importPage(request):
    return render(request, 'web/treatment/import.html', {})
