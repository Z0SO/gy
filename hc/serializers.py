from rest_framework import serializers
from .models import HistoriaClinica, ConsultaControl

class HistoriaClinicaSerializer(serializers.ModelSerializer):
 class Meta:
     model = HistoriaClinica
     fields = '__all__'

class ConsultaControlSerializer(serializers.ModelSerializer):
 class Meta:
     model = ConsultaControl
     fields = '__all__'
