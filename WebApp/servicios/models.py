from django.db import models
from django.db.models.fields import CharField, TextField, DecimalField, BooleanField


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Servicio(models.Model):
    nombre = CharField(max_length=100)
    descripcion = TextField(blank=True)
    precio = DecimalField(max_digits=10, decimal_places=2)
    activo = BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} - {self.nombre}"


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_legajo = models.IntegerField(unique=True)
    activo = BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} - {self.nombre}"


class Coordinador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_documento = models.IntegerField(unique=True)
    fecha_alta = models.DateField()
    activo = BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} - {self.nombre}"
