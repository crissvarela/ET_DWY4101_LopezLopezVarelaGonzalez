from django.db import models
from django.urls import reverse

# Create your models here.

class Oferta(models.Model):
    oferta = models.IntegerField(default=0,null=True)
    detalle = models.TextField(max_length = 300)
    fecha_oferta = models.TimeField(null=True, blank=True)
    def __str__(self):
        return f'{self.detalle} {self.oferta}%'

    def get_absolute_url (self):
        return reverse('oferta_detail',args=[str(self.id)])

class Producto(models.Model):
    precio = models.BigIntegerField(default=0,null=True)
    nombre = models.CharField(max_length = 100 )
    descripcion = models.TextField(max_length = 400)
    fecha_producto = models.DateField(null=True, blank=False)
    foto = models.ImageField(upload_to='images/', null=True, blank=True)
    oferta = models.ForeignKey('Oferta', on_delete=models.SET_NULL, null=True)
    tienda = models.ForeignKey('Tienda', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url (self):
        return reverse('producto_detail',args=[str(self.id)])

class Tienda(models.Model):
    nombre =  models.CharField(max_length = 100)
    correo = models.EmailField()
    direccion = models.CharField(max_length= 100)
    comuna = models.ForeignKey('Comuna',on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nombre
    def get_absolute_url (self):
        return reverse('tienda_detail',args=[str(self.id)])

class Comuna(models.Model):
    nombre = models.CharField(max_length= 100)
    region = models.ForeignKey('Region',on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nombre

class Region(models.Model):
    nombre = models.CharField(max_length= 100)
    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha_venta = models.DateTimeField(null=True, blank=False)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    oferta = models.ForeignKey('Oferta', on_delete=models.SET_NULL, null=True)
    tienda = models.ForeignKey('Tienda', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.fecha_venta}'
    def get_absolute_url (self):
        return reverse('venta_detail',args=[str(self.id)])
    