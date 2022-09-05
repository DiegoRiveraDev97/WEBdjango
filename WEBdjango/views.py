from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def registrarse(request):
    return render(request,'registro.html')