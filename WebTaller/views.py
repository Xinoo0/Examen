from django.shortcuts import render, redirect
from .models import Producto
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


# GESTION PRODUCTOS

def Add_Producto(request):
    codigo = request.post['txtCodigo']
    nombre = request.post['txtNombre']
    stock = request.post['numStock']
    producto = Producto.objects.create(
        codigo=codigo, nombre=nombre, stock=stock)
    messages.success(request, 'Producto Registrado')
    return redirect('/')

def Edit_Producto(request):
    codigo = request.post['txtCodigo']
    nombre = request.post['txtNombre']
    stock = request.post['numStock']
    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.stock = stock
    articulo.save()
    messages.success(request, 'Producto Actualizado')
    return redirect('/')

def Del_Producto(request):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    messages.success(request, 'Producto Eliminado')
    return redirect('/')