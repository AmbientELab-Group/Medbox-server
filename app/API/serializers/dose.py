from rest_framework import serializers
from API.models import Dose


class DoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dose
        fields = [
            "uuid",
            "treatment",
            "chamber",
            "medicine",
            "planned_administration_time",
            "number_of_pills",
            "on_demand"
        ]
