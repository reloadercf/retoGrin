from django.shortcuts import render
from rest_framework import viewsets
from .models import Scooter, Historial
from .serializers import ScooterSerializer,ScooterSerializer2,HistorialSerializer
# Create your views here.


class ScooterViewSet(viewsets.ModelViewSet):
    queryset=Scooter.objects.all()
    serializer_class=ScooterSerializer

class ScooterFiltroViewSet(viewsets.ModelViewSet):
    queryset=Scooter.objects.all()
    serializer_class=ScooterSerializer2

class HistoritalViewSet(viewsets.ModelViewSet):
    queryset=Scooter.objects.all()
    serializer_class=HistorialSerializer
