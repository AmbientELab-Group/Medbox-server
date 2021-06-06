from rest_framework.serializers import Serializer
from backend.app.AppAPI import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from AppAPI.models import Medecine
from AppAPI.serializers import (
    MedecineSerializer
)

class MedecineListCreateView(APIView):
    """
    Retrivies all medecine managed by an aunthenticated user
    """
    permission_classes = [IsAuthenticated]
    queryset = Medecine.objects.all()
    #serializer_class = MedecineSerializer

    def get_queryset(self, request):
        """
        shows only owned or managed medecine
        """
        name = self.request.query_params.get('name')
        queryset = self.queryset.filter(
            name = name,
            producer = request.user
            )
        serializer = MedecineSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        info = self.request.data
        info["name"] = self.request.user.uuid
        serializer = MedecineSerializer(data=info, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedecineDetailView(APIView):
    """
    This view jandles single medecine
    ednpoints contained in the view are retrieve, patch ,update, destroy.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Medecine.objects.get(pk=pk)
        except Medecine.DoesNotExist:
            raise status.HTTP_204_NO_CONTENT

    def get(self, request, pk):
        sample_medecine = self.get_object(pk)
        serializer = MedecineSerializer(sample_medecine)
        return Response(serializer.data)
    
    def put(self, request, pk):
        sample_medecine = self.get_object(pk)
        serializer = MedecineSerializer(sample_medecine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        sample_medecine = self.get_object(pk)
        serializer = MedecineSerializer(sample_medecine, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        sample_medicine = self.get_object(pk)
        sample_medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)