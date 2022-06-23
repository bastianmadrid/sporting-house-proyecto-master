from logging.handlers import DEFAULT_SOAP_LOGGING_PORT
from this import d
from django.db import models

# Create your models here.
class usuario(models.Model):
    """usuarioid = models.IntegerField(primary_key= True)"""
    nombre = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
class producto(models.Model):
    codigo=models.CharField(primary_key= True ,  max_length=20)
    nombre = models.CharField(max_length=20)
    descripcion= models.CharField(max_length=100)
    precio= models.IntegerField()
    def __str__(self):
        return self.nombre
    
class zapatillas(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
        
class bicileta(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
        
class equipo(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    peso = models.IntegerField()
    descripcion = models.TextField()
      
    def __str__(self):
        return self.nombre

    
    
    
        