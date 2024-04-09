from django.db import models

#modelo proveedor: nombre, apellido, dni.
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#modelo producto: nombre, precio, stock, proveedor.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre