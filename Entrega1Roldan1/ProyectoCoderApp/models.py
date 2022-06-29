from django.db import models

# Create your models here.
class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)

class Curso(models.Model):
    
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()
    
class Profesor(models.Model):
    
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    
    profesion = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "Profesores"
        
class Entregable(models.Model):
    
    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
    