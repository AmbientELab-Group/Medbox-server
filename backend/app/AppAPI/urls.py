from django.urls import path
from .views import (
    TreatmentsListCreateView,
    TreatmentsDetailView
)

urlpatterns = [
    path("treatments", TreatmentsListCreateView.as_view()),
    path("treatments/<pk>/", TreatmentsDetailView.as_view())
]
 