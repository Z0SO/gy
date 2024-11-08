
import django_filters
from .models import HistoriaClinica

class HistoriaClinicaFilter(django_filters.FilterSet):
    class Meta:
        model = HistoriaClinica
        fields = {
            # icontains es el sufijo para buscar en cualquier parte del campo
            'pac_nombre': ['icontains'],
            # exact es el sufijo para igual
            'pac_dni': ['exact'],
            # gre y lte son los sufijos para mayor o igual y menor o igual respectivamente
            'pac_edad': ['gte', 'lte'],
        }
