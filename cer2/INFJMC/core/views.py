from django.shortcuts import render
from django.http import HttpResponse

menu = "<hr><ul>"
menu +=   " <li><a href=''>Inicio</a>"
menu +=   " <li><a href='registrar/'>Registrar</a>"
menu +=   " <li><a href='administrar/'>Administrar</a>"
menu +=   " <li><a href='correspondencia/'>Correspondencia</a>"
menu +=   " <li><a href='modificar/'>Modificar</a>"
menu +=   " <li><a href='listado/'>Listado</a>"
menu += "</ul>"


def home(request):
    return render(request,'core/index.html')

def registrar(request):
    return render(request,'core/registrar.html')

def administrar(request):
    return render(request,'core/administrar.html')

def correspondencia(request):
    return render(request,'core/correspondencia.html')

def modificar(request):
    return render(request,'core/modificar.html')

def listado(request):
    return render(request,'core/listado.html')