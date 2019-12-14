from django.urls import path,include
from rest_framework import routers
from .views import ScooterViewSet,ScooterFiltroViewSet,HistoritalViewSet

scooter=routers.DefaultRouter()

scooter.register('scooter',ScooterViewSet),
scooter.register('scooter-historial',ScooterFiltroViewSet),
scooter.register('historial',HistoritalViewSet)


scooter = [
    path('scooter/', include(scooter.urls)),
]
