from django.shortcuts import render,redirect
from compra.models import Producto,Proveedor

def listado_productos(request):
    lista_productos=Producto.objects.all()
    context={
        "listado_productos":lista_productos
    }
    return render(request,"compra/listado_productos.html",context)

def listado_proveedores(request):
    lista_proveedores=Proveedor.objects.all()
    context={
        "listado_proveedores":lista_proveedores
    }
    return render(request,"compra/listado_proveedores.html",context)

def agregar_producto(request):
    lista_proveedores = Proveedor.objects.all()

    context = {
        "listado_proveedores": lista_proveedores
    }

    if request.POST:
        nombre_producto = request.POST["nombre"]
        precio_producto = request.POST["precio"]
        stock_actualP=request.POST["stock_actual"]
        proveedor_id = request.POST["proveedor"]

    
        Producto.objects.create(
            nombre=nombre_producto,
            precio=precio_producto,
            stock_actual=stock_actualP,
            proveedor=proveedor_id
        )

    return render(
        request,
        "compra/nuevo_producto.html",
        context
    )
def agregar_proveedor(request):

    if request.POST:
        nombre_proveedor = request.POST["nombre"]
        apellido_proveedor = request.POST["precio"]
        dni_proveedor = request.POST["dni"]

        Producto.objects.create(
            nombre=nombre_proveedor,
            apellido=apellido_proveedor,
            dni=dni_proveedor
        )

    return render(
        request,
        "compra/nuevo_proveedor.html"
    )

# Create your views here.
