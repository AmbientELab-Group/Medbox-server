from rest_framework import serializers
from API.models import Medicine


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            "uuid",
            "name",
            "producer",
        ]
