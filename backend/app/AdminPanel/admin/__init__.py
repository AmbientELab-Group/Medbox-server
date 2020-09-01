"""
All models.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib import admin

from .user import UserAdmin
from .medicine import MedicineAdmin
from .dose import DoseAdmin
from .treatment import TreatmentAdmin
from .predefinedTime import PredefinedTimeAdmin
from .chamber import ChamberAdmin
from .container import ContainerAdmin
from .containerVersion import ContainerVersionAdmin
from .device import DeviceAdmin
from .deviceVersion import DeviceVersionAdmin
from ..models import *

# register admin site
admin.site.register(User, UserAdmin)

# App models
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Dose, DoseAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(PredefinedTime, PredefinedTimeAdmin)

# Device models
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceVersion, DeviceVersionAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(ContainerVersion, ContainerVersionAdmin)
admin.site.register(Chamber, ChamberAdmin)


