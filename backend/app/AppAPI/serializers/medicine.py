from rest_framework import serializers
from AppAPI.models import Medicine


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            "uuid",
            "name",
            "producer",
        ]
