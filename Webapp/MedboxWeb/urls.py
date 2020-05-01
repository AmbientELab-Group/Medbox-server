"""
Medbox web application URL routing config.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "1.5.2020"

from django.contrib import admin
from django.urls import path

# authentication
from .auth.login import login
from .auth.logout import logout
from .auth.register import register

# account related
from .account.dashboard import dashboard as account_dashboard
from .account.edit import edit as account_edit
from .account.passwdChange import passwdChange as account_passwordChange
from .account.apps.dashboard import dashboard as account_apps_dashboard
from .account.apps.add import add as account_apps_add

# treatments
from .treatment.dashboard import dashboard as treatment_dashboard
from .treatment.edit import edit as treatment_edit
from .treatment.importPage import importPage as treatment_import
from .treatment.adherence import adherence as treatment_adherence

# device management
from .devices.dispensor.dashboard import dashboard as dispensor_dashboard
from .devices.dispensor.add import add as dispensor_add
from .devices.dispensor.status import status as dispensor_status
from .devices.dispensor.refill import refill as dispensor_refill

urlpatterns = [
    # for root redirect to login page
    path('', login),
    
    # explicitly admin stuff
    path('admin/', admin.site.urls), # admin panel
    
    # account management stuff
    path('auth/login', login), # login page
    path('auth/logout', logout), # logout link, go here to logout
    path('auth/register', register), # register a new user
    
    # account related pages
    path('account/dashboard', account_dashboard), # user dashboard page, you land there after login
    path('account/edit', account_edit), # user account edit page
    path('account/passwd-change', account_passwordChange), # user account password change page
    path('account/apps/dashboard', account_apps_dashboard), # paired applications dashboard
    path('account/apps/add', account_apps_add), # add new application dashboard
    
    # treatments
    path('treatment/dashboard', treatment_dashboard), # dashboard for the treatments 
    path('treatment/edit', treatment_edit), # page for the treatment edits
    path('treatment/import', treatment_import), # page for the importing treatment
    path('treatment/adherence', treatment_adherence), # page for adherence monitoring
    
    # device management
    path('devices/dispensor/dashboard', dispensor_dashboard), # dashboard page for all dispensors
    path('devices/dispensor/add', dispensor_add), # page for adding new dispensors
    path('devices/dispensor/status', dispensor_status), # page for displaying the status of new dispensors
    path('devices/dispensor/refill', dispensor_refill) # page for refilling the dispensor
]
