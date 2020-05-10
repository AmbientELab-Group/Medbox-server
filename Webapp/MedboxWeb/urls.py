"""
Medbox web application URL routing config.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "1.5.2020"

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('web/', include('Website.urls')),
    path('admin/', admin.site.urls),
]
