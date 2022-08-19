from unittest.util import _MAX_LENGTH
from django.db import models

#Modelo para la entidad TipoDocumento
class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)

#Modelo para la entidad Ciudad
class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)

#Modelo para la entidad Persona
class Persona(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    documento = models.CharField(max_length=20)
    lugarnacimiento = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fechanacimiento = models.DateField() #https://www.youtube.com/watch?v=I2-JYxnSiB0
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=15)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
