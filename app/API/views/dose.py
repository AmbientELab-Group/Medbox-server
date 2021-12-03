from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from API.serializers import DoseSerializer
from API.models import (
    Dose,
    Treatment,
    Chamber,
    Medicine,
)
from django.db.models import Q


class DoseListCreateView(generics.ListCreateAPIView):
    """
    This is a view for listing collection of doses and creating new ones.
    """
    serializer_class = DoseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Allows to show only owned or managed doses
        """
        user = self.request.user
        managed_doses = Dose.objects.filter(
            Q(chamber__container__device__owner=user) |
            Q(chamber__container__device__in=user.supervised_devices.all())
        )
        return managed_doses

    def list(self, request):
        """
        This endpoint returns all owned or managed doses for authenticated
        user.
        """
        doses = self.get_queryset()
        chamber_UUID = request.query_params.get("chamber")
        serializer = self.get_serializer(doses, many=True)

        if chamber_UUID is not None:
            requested_doses = doses.filter(chamber__uuid=chamber_UUID)

            if not requested_doses:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = self.get_serializer(requested_doses, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        This endpoint allows to create new doses.
        """
        chamber_UUID = request.data.get("chamber")
        chamber = Chamber.objects.get(uuid=chamber_UUID)
        treatment_UUID = request.data.get("treatment")
        treatment = Treatment.objects.get(uuid=treatment_UUID)
        medicine_UUID = request.data.get("medicine")
        medicine = Medicine.objects.get(uuid=medicine_UUID)

        if not chamber or not treatment or not medicine:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DoseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This is a view for managing a single dose (retrieve, update, destroy)
    """
    serializer_class = DoseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Allows to show only owned or managed doses
        """
        user = self.request.user
        managed_doses = Dose.objects.filter(
            Q(chamber__container__device__owner=user) |
            Q(chamber__container__device__in=user.supervised_devices.all())
        )
        return managed_doses
