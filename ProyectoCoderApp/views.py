import datetime

from django.shortcuts import render
from django.http import HttpResponse

from ProyectoCoderApp.models import *

# Create your views here.
def inicio(request):
    
    nombre = " Santi"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]
   
    return render(request,"index.html",{"mi_nombre":nombre,"dia_hora": hoy, "notas": notas})

def crear_juego(request):
    
    juego = "Modern Warfare"
    grupo = "7709"
    
    nuevo_juego = Juego(juego=juego, grupo=grupo)
    nuevo_juego.save()
    
    return HttpResponse(f"Hemos agregado el juego de {juego} con comisión {grupo}")

def lideres(request):
    
    return render(request, "/Users/eloso/PYTH/ProyectoCoder/ProyectoCoderApp/templatess/ProyectoCoderApp/lideres.html",{})

def jugadores(request):
    
    return render(request, "/Users/eloso/PYTH/ProyectoCoder/ProyectoCoderApp/templatess/ProyectoCoderApp/jugadores.html",{})

def juegos(request):
    
    juegos = Juego.objects.all()
    #return HttpResponse("Vista de cursos")
    return render(request,"/Users/eloso/PYTH/ProyectoCoder/ProyectoCoderApp/templatess/ProyectoCoderApp/juegos.html",{"juegos":juegos})
 
def base(request):
    
    return render(request,"/Users/eloso/PYTH/ProyectoCoder/ProyectoCoderApp/templatess/ProyectoCoderApp/base.html",{})