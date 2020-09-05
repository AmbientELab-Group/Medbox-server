"""
Medbox server main routing config.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "1.5.2020"

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/', include('AdminPanel.urls')),
    path('admin/', admin.site.urls),
    path('api/device/', include('DeviceAPI.urls')),
    path('api/app/', include('AppAPI.urls'))
]
