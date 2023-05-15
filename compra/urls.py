from django.urls import path

from.views import listado_productos,agregar_producto,agregar_proveedor

urlpatterns=[
    path("listado_productos/",listado_productos,name="listado_productos"),
    path("productos/nuevo",agregar_producto,name="agregar_producto"),
    path("proveedores/nuevo",agregar_proveedor,name="agregar_proveedor")
]