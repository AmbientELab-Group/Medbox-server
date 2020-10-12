from rest_framework import serializers
from AppAPI.models import Dose


class DoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dose
        fields = [
            "uuid",
            "treatment",
            "chamber",
            "medicine",
            "plannedAdministrationTime",
            "numberOfPills",
            "onDemand"
        ]

