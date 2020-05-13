"""
Medbox website application URL routing config.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "10.5.2020" 

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
    
    # account management stuff
    path('auth/login', login, name='login-page'), # login page
    path('auth/logout', logout, name='logout-page'), # logout link, go here to logout
    path('auth/register', register, name='registration-page'), # register a new user
    
    # account related pages
    path('account/dashboard', account_dashboard, name='user-dashboard'), # user dashboard page, you land there after login
    path('account/edit', account_edit, name='user-account-edit'), # user account edit page
    path('account/passwd-change', account_passwordChange, name='user-password-change'), # user account password change page
    path('account/apps/dashboard', account_apps_dashboard, name='user-apps-dashboard'), # paired applications dashboard
    path('account/apps/add', account_apps_add, name='user-apps-add'), # add new application dashboard
    
    # treatments
    path('treatment/dashboard', treatment_dashboard, name='treatment-dashboard'), # dashboard for the treatments 
    path('treatment/edit', treatment_edit, name='treatment-edit'), # page for the treatment edits
    path('treatment/import', treatment_import, name='treatment-import'), # page for the importing treatment
    path('treatment/adherence', treatment_adherence, name='treatment-adherence'), # page for adherence monitoring
    
    # device management
    path('devices/dispensor/dashboard', dispensor_dashboard, name='devices-dispensor-dashboard'), # dashboard page for all dispensors
    path('devices/dispensor/add', dispensor_add, name='devices-dispensor-add'), # page for adding new dispensors
    path('devices/dispensor/status', dispensor_status, name='devices-dispensor-status'), # page for displaying the status of new dispensors
    path('devices/dispensor/refill', dispensor_refill, name='devices-dispensor-refill') # page for refilling the dispensor
]
