from django.contrib import admin

# Register your models here.
#usamos los modelos creados previamente p'ara construir automaticamente
#un area dentro del sistema q uso para crear consultar actualizar y borrrar registros

from django.contrib import admin

from compra.models import Producto,Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor

    # muestra la info en columnas en el admin
    list_display = [
        "id",
        "nombre",
        "apellido",
        "dni"
    ]

    # busqueda por fields
    search_fields = [
        "nombre",
        "apellido",
        "dni"
    ]


class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = [
        "id",
        "nombre",
        "precio",
        "stock_actual",
        "proveedor",
    ]
    search_fields = [
        "nombre",
        "proveedor__nombre"
    ]

    # filtros: se despliega a la izquierda del admin
    list_filter = [
        "proveedor__nombre"
        #"activo",
    ]

    # campos de solo lectura
   # readonly_fields = [
   #     "precio",
   #     "activo"
   # ]


# registrar modelos
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)