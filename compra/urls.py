from django.urls import path

from.views import (listado_productos,
listado_proveedores,
agregar_producto,
agregar_proveedor,)


urlpatterns=[
    path("listado_productos/",listado_productos,name="listado_productos"),
    path("listado_proveedores/",listado_proveedores,name="listado_proveedores"),
    path("productos/nuevo",agregar_producto,name="agregar_producto"),
    path("proveedores/nuevo",agregar_proveedor,name="agregar_proveedor")

]