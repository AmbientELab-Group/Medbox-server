from django.contrib import admin
from .user import UserAdmin
from .medicine import MedicineAdmin
from .dose import DoseAdmin
from .treatment import TreatmentAdmin
from .predefinedTime import PredefinedTimeAdmin
from .chamber import ChamberAdmin
from .container import ContainerAdmin
from .device import DeviceAdmin
from ..models import *

admin.site.register(User, UserAdmin)

admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Dose, DoseAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(PredefinedTime, PredefinedTimeAdmin)

admin.site.register(Device, DeviceAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Chamber, ChamberAdmin)
