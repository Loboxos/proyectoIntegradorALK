from django.urls import path

from.views import listado_productos,agregar_producto

urlpatterns=[
    path("listado_productos/",listado_productos,name="listado_productos"),
    path("productos/nuevo",agregar_producto,name="agregar_producto")
]