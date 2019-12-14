from rest_framework import serializers
from .models import Scooter, Historial

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Historial
        fields='__all__'

class ScooterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scooter
        fields='__all__'

class ScooterSerializer2(serializers.ModelSerializer):
    moviliario=HistorialSerializer(many=True, read_only=True)
    class Meta:
        model=Scooter
        fields='__all__'