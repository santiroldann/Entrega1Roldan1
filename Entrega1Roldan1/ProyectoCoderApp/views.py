import datetime

from django.shortcuts import render
from django.http import HttpResponse

from ProyectoCoderApp.models import Curso

# Create your views here.
def inicio(request):
    
    nombre = " Santi"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]
   
    return render(request,"index.html",{"mi_nombre":nombre,"dia_hora": hoy, "notas": notas})

def crear_curso(request):
    
    nombre = "Python"
    comision = "31080"
    
    nuevo_curso = Curso(nombre=nombre, comision=comision)
    nuevo_curso.save()
    
    return HttpResponse(f"Hemos agregado el curso de {nombre} con comisión {comision}")

def profesores(request):
    
    return render(request, "/Users/eloso/PYTH/ProyectoCoder/ProyectoCoderApp/templatess/ProyectoCoderApp/profesores.html",{})

def estudiantes(request):
    
    return render(request, "/Users/eloso/PYTH/ProyectoCoder/ProyectoCoderApp/templatess/ProyectoCoderApp/estudiantes.html",{})

def cursos(request):
    
    cursos = Curso.objects.all()
    #return HttpResponse("Vista de cursos")
    return render(request,"/Users/eloso/PYTH/ProyectoCoder/ProyectoCoderApp/templatess/ProyectoCoderApp/cursos.html",{"cursos":cursos})

def entregables(request):
    
    return render(request, "/Users/eloso/PYTH/ProyectoCoder/ProyectoCoderApp/templatess/ProyectoCoderApp/entregables.html", {})

def base(request):
    
    return render(request,"/Users/eloso/PYTH/ProyectoCoder/ProyectoCoderApp/templatess/ProyectoCoderApp/base.html",{})