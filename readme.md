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


-manejare las urls creando una la app llamado api 
