#from backend.app.AppAPI.views.medecines import MedecineDetailView, MedecineListCreateView
from django.urls import path
from .views import (
    TreatmentsListCreateView,
    TreatmentsDetailView,
    MedicineListCreateView,
    MedicineDetailView
)

urlpatterns = [
    path("treatments/", TreatmentsListCreateView.as_view()),
    path("treatments/<pk>", TreatmentsDetailView.as_view()),
    path("medicines/", MedicineListCreateView.as_view()),
    path("medicines/<pk>", MedicineDetailView.as_view())
]
 