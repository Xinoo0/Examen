from django.shortcuts import render, redirect
from .models import Auto
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.


#def base(request):
#    context={}
#    return render(request, 'Web/base.html', context)

def index(request):
    context={}
    return render(request, 'Web/index.html', context)

def nosotros(request):
    context={}
    return render(request, 'Web/nosotros.html', context)

def europeas(request):
    context={}
    return render(request, 'Web/Europeas.html', context)

def marcas(request):
    context={}
    return render(request, 'Web/marcas.html', context)

def tienda(request):
    context={}
    return render(request, 'Web/tienda.html', context)

# GESTION USUARIOS

def login(request):
    return render(request, 'registration/login.html')

def salir(request):
    logout(request)
    return redirect('/')