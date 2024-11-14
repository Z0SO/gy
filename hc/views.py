from rest_framework import viewsets
from .models import HistoriaClinica, ConsultaControl
from .serializers import HistoriaClinicaSerializer, ConsultaControlSerializer
from .filters import HistoriaClinicaFilter
from django_filters.rest_framework import DjangoFilterBackend   # Importamos el filtro de django para usarlo en el viewset


class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer
    
    # Definimos el filtro de django para usarlo en el viewset
    filter_backends = [DjangoFilterBackend]

    filterset_class = HistoriaClinicaFilter

class ConsultaControlViewSet(viewsets.ModelViewSet):
    queryset = ConsultaControl.objects.all()
    serializer_class = ConsultaControlSerializer
   
    # Definimos el filtro de django para usarlo en el viewset
    filter_backends = [DjangoFilterBackend]
    
    filterset_fields = ['historia_clinica']  # Definimos los campos por los cuales se va a filtrar
