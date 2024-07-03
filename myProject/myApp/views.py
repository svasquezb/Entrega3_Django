from django.shortcuts import render

def index(request):
    context={}
    return render(request, "myApp/index.html", context)

def productos(request):
    context={}
    return render(request, "myApp/productos.html", context)

def login(request):
    context={}
    return render(request, "myApp/login.html", context)

def register(request):
    context={}
    return render(request, "myApp/register.html", context)

def carro(request):
    context={}
    return render(request, "myApp/carro.html", context)

def detalleJuego(request):
    context={}
    return render(request, "myApp/detalleJuego.html", context)