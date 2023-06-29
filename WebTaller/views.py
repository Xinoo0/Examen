from django.shortcuts import render, redirect
from .models import Auto
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.


def index(request):
    context={}
    return render(request, 'Web/index.html', context)

def nosotros(request):
    context={}
    return render(request, 'Web/nosotros.html', context)


# GESTION USUARIOS

def login(request):
    return render(request, 'registration/login.html')

def salir(request):
    logout(request)
    return redirect('/')