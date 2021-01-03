from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from AppAPI.models import Treatment
from AppAPI.serializers import (
    TreatmentSerializer
)


class TreatmentsListCreateView(APIView):
    """
    Shows all treatments managed by a certain user
    """
    permission_classes = [IsAuthenticated]
    queryset = Treatment.objects.all()

    def get(self, request):
        beneficiary = self.request.query_params.get('beneficiary')
        queryset = self.queryset.filter(
            beneficiary=beneficiary,
            associated_user=request.user
            )
        serializer = TreatmentSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        info = self.request.data
        info["associated_user"] = self.request.user.uuid
        serializer = TreatmentSerializer(data=info, many=False)
        #serializer["associated_user"] = self.request.user
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TreatmentsDetailView(APIView):
    """
    View for managing single treatement.
    Contains retrive, update, patch and destroy endpoints.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Treatment.objects.get(pk=pk)
        except Treatment.DoesNotExist:
            raise status.HTTP_204_NO_CONTENT

    def get(self, request, pk):
        treat = self.get_object(pk)
        serializer = TreatmentSerializer(treat)
        return Response(serializer.data)
   
    def put(self, request, pk):
        treat = self.get_object(pk)
        serializer = TreatmentSerializer(treat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        treat = self.get_object(pk)
        serializer = TreatmentSerializer(treat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        treat = self.get_object(pk)
        treat.delete()
        return Response(status=status.HTTP_200_OK)