from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from AppAPI.models import Medicine
from AppAPI.serializers import (
    MedicineSerializer
)

class MedicineListCreateView(APIView):
    """
    Retrivies all medicine managed by an aunthenticated user
    """
    permission_classes = [IsAuthenticated]
    queryset = Medicine.objects.all()
    #serializer_class = MedicineSerializer

    def get_queryset(self, request):
        """
        shows only owned or managed medicine
        """
        name = self.request.query_params.get('name')
        queryset = self.queryset.filter(
            name = name,
            producer = request.user
            )
        serializer = MedicineSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        info = self.request.data
        info["name"] = self.request.user.uuid
        serializer = MedicineSerializer(data=info, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicineDetailView(APIView):
    """
    This view jandles single medicine
    ednpoints contained in the view are retrieve, patch ,update, destroy.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise status.HTTP_204_NO_CONTENT

    def get(self, request, pk):
        sample_medicine = self.get_object(pk)
        serializer = MedicineSerializer(sample_medicine)
        return Response(serializer.data)
    
    def put(self, request, pk):
        sample_medicine = self.get_object(pk)
        serializer = MedicineSerializer(sample_medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        sample_medicine = self.get_object(pk)
        serializer = MedicineSerializer(sample_medicine, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        sample_medicine = self.get_object(pk)
        sample_medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)