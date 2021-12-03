from rest_framework import serializers
from API.models import Treatment


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = [
            "uuid",
            "associated_user",
            "name",
            "beneficiary",
        ]
