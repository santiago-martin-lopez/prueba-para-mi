from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def clientes(request):
    if request.method=="POST":
        form=Formucliente(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            email=informacion["email"]
            telefono=informacion["telefono"]
            direccion=informacion['direccion']
            cliente1= Cliente(nombre_cliente=nombre, email_cliente=email, telefono_cliente=telefono,direccion_cliente=direccion)
            cliente1.save()
            return render (request, "inicio.html", {"mensaje": "cliente cargado correctamente"})
    else:
        formulario=Formucliente()

    return render(request,'paginaclientes.html',{'form':formulario})

def articulos(request):
    if request.method=="POST":
        form=Formuarticulo(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            categoria=informacion['categoria']
            precio=informacion['precio']
            articulo1= Articulos(nombre_articulo=nombre,categoria_articulo=categoria,precio_articulo=precio)
            articulo1.save()
            return render (request, "inicio.html", {"mensaje": "articulo cargado correctamente"})
    else:
        formulario=Formuarticulo()

    return render(request,'paginaarticulos.html',{'form':formulario})

def pedidos(request):
    if request.method=="POST":
        form=Formupedidos(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            fecha=informacion['fecha']
            entrega=informacion['entrega']
            codigo_seguimiento=informacion['codigo_seguimiento']
            pedido1= Pedidos(fecha_pedido=fecha,entrega_pedido=entrega,codigo_seguimiento=codigo_seguimiento)
            pedido1.save()
            return render (request, "inicio.html", {"mensaje": "pedido cargado correctamente"})
    else:
        formulario=Formupedidos()

    return render(request,'paginapedidos.html',{'form':formulario})

def busquedaclientes(request):
    return render(request, "busquedaclientes.html")


def resultadosclientes(request):
    if request.GET['nombre_cliente']:
        busqueda=request.GET['nombre_cliente']
        clientes=Cliente.objects.filter(nombre_cliente__icontains=busqueda)
        return render(request,"resultadosclientes.html", {'clientes':clientes} )
    else:
        return render(request, "busquedaclientes.html", {"mensaje":"busca un cliente"})

def busquedaarticulos(request):
    return render(request,'busquedaarticulos.html')

def resultadosarticulos(request):
    if request.GET['categoria_articulo']:
        busqueda=request.GET['categoria_articulo']
        articulos=Articulos.objects.filter(categoria_articulo__icontains=busqueda)
        return render(request,"resultadosarticulos.html", {'articulos':articulos} )
    else:
        return render(request, "busquedaarticulos.html", {"mensaje":"busca un articulo valido"})

