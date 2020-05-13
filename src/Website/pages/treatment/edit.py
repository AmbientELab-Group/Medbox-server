from django.shortcuts import render

def edit(request):
    return render(request, 'web/treatment/edit.html', {})
