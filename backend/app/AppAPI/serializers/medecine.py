from rest_framework import serializers
from AppAPI.models import Medecine


class MedecineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecine
        fields = [
            "uuid",
            "name",
            "producer",
        ]
