from rest_framework import viewsets
from .models import HistoriaClinica, ConsultaControl
from .serializers import HistoriaClinicaSerializer, ConsultaControlSerializer

class HistoriaClinicaViewSet(viewsets.ModelViewSet):
 queryset = HistoriaClinica.objects.all()
 serializer_class = HistoriaClinicaSerializer

class ConsultaControlViewSet(viewsets.ModelViewSet):
 queryset = ConsultaControl.objects.all()
 serializer_class = ConsultaControlSerializer
