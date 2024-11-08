from django.db import models


class HistoriaClinica(models.Model):
    pac_dni = models.CharField(max_length=8, unique=True) 
    pac_nombre = models.CharField(max_length=50)
    pac_edad = models.IntegerField()
    pac_domicilio = models.CharField(max_length=100)
    pac_obrasocial = models.CharField(max_length=50)
    pac_telefono = models.CharField(max_length=15)
    pac_telefono_emergencia = models.CharField(max_length=15)
    pac_ocupacion = models.CharField(max_length=50)
    pac_estadocivil = models.CharField(max_length=50)

    motivo_consulta = models.TextField()
    derivado_por = models.CharField(max_length=50)
    antecedentes_clinicos = models.TextField()
    
    hc_laboratorio = models.TextField(blank=True, null=True)
    
    diagnostico_presuntivo = models.TextField()
    tratamientos_anteriores = models.TextField()
    tratamiento_actual = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historia Clínica de {self.pac_nombre}"


class ConsultaControl(models.Model):
    historia_clinica = models.ForeignKey(HistoriaClinica, related_name='revisiones', on_delete=models.CASCADE)
    fecha_evaluacion = models.DateTimeField(auto_now_add=True)
    
    cc_laboratorio = models.TextField(blank=True, null=True)
    
    estado_actual = models.TextField()
    indicaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Revisión de {self.historia_clinica.pac_nombre} - {self.fecha_evaluacion.strftime('%Y-%m-%d')}"
