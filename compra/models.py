from django.db import models

class Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nombre},{self.apellido}"

class Producto(models.Model):
    nombre=models.CharField(max_length=25)
    precio=models.FloatField(default=0)
    stock_actual=models.IntegerField(default=0)
    proveedor=models.ForeignKey(Proveedor,related_name="proveedor",on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre}\n{self.precio}\n{self.stock_actual}\n{self.proveedor}"
# Create your models here.
