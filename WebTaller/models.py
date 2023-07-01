from django.db import models

# Create your models here.


class Auto(models.Model):
    patente = models.CharField(primary_key=True, max_length=6 )
    marca   = models.CharField(max_length=20)
    modelo  = models.CharField(max_length=20)
    año     = models.DateField(blank=False, null=False)


class Cliente(models.Model):
    rut    = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    ap_paterno = models.CharField(max_length=20)
    ap_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    
class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    stock = models.PositiveSmallIntegerField()
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.stock)