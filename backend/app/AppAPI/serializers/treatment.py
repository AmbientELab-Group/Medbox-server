from rest_framework import serializers
from AppAPI.models import Treatment


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = [
            "uuid",
            "associated_user",
            "name",
            "beneficiary",
        ]
