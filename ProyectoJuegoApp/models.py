from django.db import models

# Create your models here.
class Jugador(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Jugadores"

class Juego(models.Model):
    
    juego = models.CharField(max_length=30)
    grupo = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Juegos"
    
class Lider(models.Model):
    
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    
    juego = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "Lideres"
        

    