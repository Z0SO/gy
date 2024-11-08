from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoriaClinicaViewSet, ConsultaControlViewSet

router = DefaultRouter()
router.register(r'historias_clinicas', HistoriaClinicaViewSet)
router.register(r'consultas_control', ConsultaControlViewSet)

urlpatterns = [
 path('api/', include(router.urls)),
]
