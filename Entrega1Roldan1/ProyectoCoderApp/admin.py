from django.contrib import admin

from .models import *
from ProyectoCoderApp.views import estudiantes

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    
    list_display = ("nombre","comision")
    search_fields = ("nombre", "comision")
    
class EstudianteAdmin(admin.ModelAdmin):
    
    list_display = ("nombre","apellido")
    
class ProfesorAdmin(admin.ModelAdmin):
    
    list_display = ("nombre","apellido","profesion")
    
class EntregableAdmin(admin.ModelAdmin):
    
    list_display = ("nombre","fechaEntrega","entregado")
    

admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Entregable, EntregableAdmin)


                