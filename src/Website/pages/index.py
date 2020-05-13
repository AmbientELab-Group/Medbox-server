"""
View for index page.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "13.5.2020" 

from django.shortcuts import redirect

# just reirect to login page for now
def index(request):
    return redirect('login-page') 
