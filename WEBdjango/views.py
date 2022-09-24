from urllib import request
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def registrarse(request):
    return render(request,'registro.html')
    
def quienesSomos(request):
    return render(request,'quienesSomos.html')

def productos2(request):
    return render(request,'productos2.html')

def productos(request):
    return render(request,'productos.html')

def servicios(request):
    return render(request,'servicios.html')

def servicios2(request):
    return render(request,'servicios2.html')

def vision(request):
    return render(request,'vision.html')

def contactenos(request):
    return render(request,'contactenos.html')