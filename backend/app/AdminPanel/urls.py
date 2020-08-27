"""
Medbox website application URL routing config.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "10.5.2020"

from django.urls import path
# from . import pages

urlpatterns = [
#     # for root redirect to login page
#     path('', pages.index, name='index'),
    
    # login page
#     path('auth/login', pages.auth.login, name='login-page'),
    
#     # logout link
#     path('auth/logout', pages.auth.logout, name='logout-page'),
    
#     # register a new user
#     path('auth/register', pages.auth.register, name='registration-page'),
    
#     # user dashboard page, you land there after login
#     path('account/dashboard', pages.account.dashboard, name='user-dashboard'),
    
#     # user account edit page
#     path('account/edit', pages.account.edit, name='user-account-edit'),
    
#     # user account password change page
#     path('account/passwd-change', pages.account.passwdChange,
#          name='user-password-change'),
    
#     # paired applications dashboard
#     path('account/apps/dashboard', pages.account.apps.dashboard,
#          name='user-apps-dashboard'),
    
#     # add new application dashboard
#     path('account/apps/add', pages.account.apps.add, name='user-apps-add'),
    
#     # dashboard for the treatments
#     path('treatment/dashboard', pages.treatment.dashboard,
#          name='treatment-dashboard'),
    
#     # page for the treatment edits
#     path('treatment/<str:treatmentID>/edit', pages.treatment.edit,
#          name='treatment-edit'),
    
#     # page for exporting tokens
#     path('treatment/<str:treatmentID>/exportToken',
#          pages.treatment.exportToken, name='treatment-export-token'),
    
#     # page for editing medicine
#     path('treatment/<str:treatmentID>/medicine/<str:medicineID>/edit',
#          pages.treatment.medicine.edit, name='treatment-medicine-edit'),
    
#     # page for deliting medicine
#     path('treatment/<str:treatmentID>/medicine/<str:medicineID>/delete',
#          pages.treatment.medicine.delete, name='treatment-medicine-delete'),
    
#     # page for the importing treatment
#     path('treatment/import', pages.treatment.importPage, name='treatment-import'),
    
#     # page for adherence monitoring
#     path('treatment/adherence', pages.treatment.adherence,
#          name='treatment-adherence'),
    
#     # dashboard page for all dispensors
#     path('devices/dispensor/dashboard', pages.devices.dispensor.dashboard,
#          name='devices-dispensor-dashboard'),
    
#     # page for adding new dispensors
#     path('devices/dispensor/add', pages.devices.dispensor.add,
#          name='devices-dispensor-add'),
    
#     # page for deleting dispensors
#     path('devices/dispensor/<str:dispensorID>/delete',
#          pages.devices.dispensor.delete, name='devices-dispensor-delete'),
    
#     # page for displaying the status of new dispensors
#     path('devices/dispensor/status', pages.devices.dispensor.status,
#          name='devices-dispensor-status'),
    
#     # page for refilling the dispensor
#     path('devices/dispensor/refill', pages.devices.dispensor.refill,
#          name='devices-dispensor-refill')
]
