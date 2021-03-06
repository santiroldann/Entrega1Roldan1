from django.contrib import admin

from .models import *
from ProyectoJuegoApp.views import *

# Register your models here.

class JuegoAdmin(admin.ModelAdmin):
    
    list_display = ("juego","grupo")
    search_fields = ("juego", "grupo")
    
class JugadorAdmin(admin.ModelAdmin):
    
    list_display = ("nombre","apellido")
    
class LiderAdmin(admin.ModelAdmin):
    
    list_display = ("nombre","apellido","juego")
    
    

admin.site.register(Juego, JuegoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Lider, LiderAdmin)


                