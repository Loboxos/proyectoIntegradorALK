# Proyecto Integrador Individual

## Poner en marcha el proyecto: ##

-Crea el virtualvenv : ```python3 o python -m venv "nombre-entorno-vir"```

-Activar el virtualenv: ``` "nombre-entorno"vir"\Scripts\activate```

-Instalar dependencias : ```pip install -r requirements.txt```

-ejecutar el servidor : ``` python3 o python manage.py runserver ```

-ir a la url localhost:8000

## trabajo realizado
-posteriormente creacion de modelos "Producto" y "Proveedor"
-genera archivos de migraciones a partir de modelos ```python3 manage.py makemigrations ```
-creacion de las tablas en la base de datos y aplicacion ```python manage.py migrate ``` esto con el uso de ORM de Django ```python manage.py shell```
![ejemploORM](https://github.com/Loboxos/proyectoIntegradorALK/assets/100051726/9598fa24-7a4c-4439-9291-de6d418e52ab)


-manejare las urls que devuelva datos de la base de datos 
en formato json con la app llamado api 

-tambien usaremos jinja para sistema de templates``` pip install jinja2```

-usamos bootstrap

-algunos urls:    localhost:8000/compra/listado_productos/ [name='listado_productos']
                  localhost:8000/compra/listado_proveedores/ [name='listado_proveedores']
                  localhost:8080/compra/productos/nuevo [name='agregar_producto']
                  localhost:8080/compra/proveedores/nuevo[name='agregar_proveedores']

-algunas vistas:  

#LISTADO PRODUCTOS
![image](https://github.com/Loboxos/proyectoIntegradorALK/assets/100051726/2f02b910-2eaa-40a7-bafb-c80b2a604678)
#LISTADO PROVEEDORES
![image](https://github.com/Loboxos/proyectoIntegradorALK/assets/100051726/08d7c566-0763-400d-b858-ca57ae66b829)
#AGREGAR UN NUEVO PRODUCTO
![image](https://github.com/Loboxos/proyectoIntegradorALK/assets/100051726/623c2615-bccc-4315-8ab7-7178721b8a34)
#AGREGAR UN NUEVO PROVEEDOR
![image](https://github.com/Loboxos/proyectoIntegradorALK/assets/100051726/dd2b8384-1125-4c7d-8217-827e8447a7a7)

-vistas desde admin
![image](https://github.com/Loboxos/proyectoIntegradorALK/assets/100051726/f01b9da3-a926-44e5-b304-4083c95aba98)
![image](https://github.com/Loboxos/proyectoIntegradorALK/assets/100051726/889a6428-0fba-44dd-850a-ffd7fa3d0d98)

-vistas desde base de datos
![image](https://github.com/Loboxos/proyectoIntegradorALK/assets/100051726/6ab0982b-a2eb-430a-9608-cf9cd669019b)
![image](https://github.com/Loboxos/proyectoIntegradorALK/assets/100051726/20d34874-de1d-490c-adbf-f4e201c50a54)
