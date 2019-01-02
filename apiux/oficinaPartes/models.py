from django.db import models
from viewflow.models import Process
from datetime import datetime

# Create your models here.
class OficinaPartesProcess(Process):
    remitente = models.CharField(max_length=250)
    institucion = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=250)
    fecha = models.DateTimeField
    jefe = models.CharField(max_length=250)
    mejoramigo = models.CharField(max_length=250)
    approved = models.BooleanField(default=False)

class VacacionesProcess(Process):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    fecha_nacimiento = models.DateTimeField(default=datetime.now(), blank=True)
    document = models.FileField(upload_to='documents/')

class Empleado(models.Model):
    nombre = models.CharField(max_length=250)