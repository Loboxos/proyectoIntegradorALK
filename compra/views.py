from django.shortcuts import render,redirect
from compra.models import Producto,Proveedor

def listado_productos(request):
    lista_productos=Producto.objects.all()
    context={
        "listado_productos":lista_productos
    }

# Create your views here.
