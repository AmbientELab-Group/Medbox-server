from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import ChamberSerializer
from DeviceAPI.models import Chamber
from django.db.models import Q


class ChamberList(generics.ListAPIView):
    """
    This is a view for listing collection of chambers
    """
    serializer_class = ChamberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Allows to show only owned or managed chambers
        """
        user = self.request.user
        managed_chambers = Chamber.objects.filter(
            Q(container__device__owner=user) |
            Q(container__device__in=user.supervised_devices.all())
        )
        return managed_chambers

    def list(self, request):
        """
        This endpoint returns all owned or mananaged chambers
        by authenticated user or those from the container specified
        in query parameter.
        """
        queryset = self.get_queryset()
        container = request.query_params.get("container")

        if container is not None:
            queryset = queryset.filter(container=container)
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ChamberDetail(generics.RetrieveAPIView):
    """
    This is a view for showing a single chamber
    """
    serializer_class = ChamberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Allows to show only owned or managed chambers
        """
        user = self.request.user
        managed_chambers = Chamber.objects.filter(
            Q(container__device__owner=user) |
            Q(container__device__in=user.supervised_devices.all())
        )
        return managed_chambers
