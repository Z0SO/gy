# Generated by Django 5.1.3 on 2024-11-08 03:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pac_dni', models.CharField(max_length=8, unique=True)),
                ('pac_nombre', models.CharField(max_length=50)),
                ('pac_edad', models.IntegerField()),
                ('pac_domicilio', models.CharField(max_length=100)),
                ('pac_obrasocial', models.CharField(max_length=50)),
                ('pac_telefono', models.CharField(max_length=15)),
                ('pac_telefono_emergencia', models.CharField(max_length=15)),
                ('pac_ocupacion', models.CharField(max_length=50)),
                ('pac_estadocivil', models.CharField(max_length=50)),
                ('motivo_consulta', models.TextField()),
                ('derivado_por', models.CharField(max_length=50)),
                ('antecedentes_clinicos', models.TextField()),
                ('hc_laboratorio', models.TextField(blank=True, null=True)),
                ('diagnostico_presuntivo', models.TextField()),
                ('tratamientos_anteriores', models.TextField()),
                ('tratamiento_actual', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConsultaControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_evaluacion', models.DateTimeField(auto_now_add=True)),
                ('cc_laboratorio', models.TextField(blank=True, null=True)),
                ('estado_actual', models.TextField()),
                ('indicaciones', models.TextField(blank=True, null=True)),
                ('historia_clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisiones', to='hc.historiaclinica')),
            ],
        ),
    ]