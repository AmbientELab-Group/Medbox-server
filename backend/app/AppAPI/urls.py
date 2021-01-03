from django.urls import path
from .views import (
    TreatmentsListCreateView,
    TreatmentsDetailView
)

urlpatterns = [
    path("api/treatments", TreatmentsListCreateView.as_view()),
    path("api/treatments/<pk>/", TreatmentsDetailView.as_view())
]
