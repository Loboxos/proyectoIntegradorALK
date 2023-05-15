from django.shortcuts import render,redirect
from compra.models import Producto,Proveedor

def listado_productos(request):
    lista_productos=Producto.objects.all()
    context={
        "listado_productos":lista_productos
    }
    return render(request,"compra/listado_productos.html",context)
# Create your views here.
