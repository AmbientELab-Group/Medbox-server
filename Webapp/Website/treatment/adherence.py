from django.shortcuts import render

def adherence(request):
   return render(request, 'web/treatment/adherence.html', {})
