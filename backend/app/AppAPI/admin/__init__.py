from django.contrib import admin

from .medicine import MedicineAdmin
from .dose import DoseAdmin
from .treatment import TreatmentAdmin
from .predefinedTime import PredefinedTimeAdmin

from ..models import (
    Treatment,
    Dose,
    Medicine,
    PredefinedTime
)

admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Dose, DoseAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(PredefinedTime, PredefinedTimeAdmin)
