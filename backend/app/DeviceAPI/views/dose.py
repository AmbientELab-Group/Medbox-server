from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import (
    Dose,
    ContainerCreateOnlySerializer
)
from DeviceAPI.models import Dose, Device
from django.db.models import Q
