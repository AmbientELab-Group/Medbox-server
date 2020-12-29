from django.urls import path
from .views import (
    TreatmentsListCreateView
)

urlpatterns = [
    path("api/treatments", TreatmentsListCreateView.as_view())
]
