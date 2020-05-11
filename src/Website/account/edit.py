from django.shortcuts import render

def edit(request):
    return render(request, 'web/account/edit.html', {})

