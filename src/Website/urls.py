"""
Medbox website application URL routing config.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "10.5.2020" 

from django.urls import path

from . import pages

urlpatterns = [
    # for root redirect to login page
    path('', pages.index, name='index'),
    
    # account management stuff
    path('auth/login', pages.auth.login, name='login-page'), # login page
    path('auth/logout', pages.auth.logout, name='logout-page'), # logout link, go here to logout
    path('auth/register', pages.auth.register, name='registration-page'), # register a new user
    
    # account related pages
    path('account/dashboard', pages.account.dashboard, name='user-dashboard'), # user dashboard page, you land there after login
    path('account/edit', pages.account.edit, name='user-account-edit'), # user account edit page
    path('account/passwd-change', pages.account.passwdChange, name='user-password-change'), # user account password change page
    path('account/apps/dashboard', pages.account.apps.dashboard, name='user-apps-dashboard'), # paired applications dashboard
    path('account/apps/add', pages.account.apps.add, name='user-apps-add'), # add new application dashboard
    
    # treatments
    path('treatment/dashboard', pages.treatment.dashboard, name='treatment-dashboard'), # dashboard for the treatments 
    path('treatment/edit/<str:treatmentID>', pages.treatment.edit, name='treatment-edit'), # page for the treatment edits
    path('treatment/import', pages.treatment.importPage, name='treatment-import'), # page for the importing treatment
    path('treatment/adherence', pages.treatment.adherence, name='treatment-adherence'), # page for adherence monitoring
    
    # device management
    path('devices/dispensor/dashboard', pages.devices.dispensor.dashboard, name='devices-dispensor-dashboard'), # dashboard page for all dispensors
    path('devices/dispensor/add', pages.devices.dispensor.add, name='devices-dispensor-add'), # page for adding new dispensors
    path('devices/dispensor/status', pages.devices.dispensor.status, name='devices-dispensor-status'), # page for displaying the status of new dispensors
    path('devices/dispensor/refill', pages.devices.dispensor.refill, name='devices-dispensor-refill') # page for refilling the dispensor
]
