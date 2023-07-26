from django.db import models
from django.contrib.auth.models import User

# All models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

class Pedido(models.Model):
    fecha_hora_pedido = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
