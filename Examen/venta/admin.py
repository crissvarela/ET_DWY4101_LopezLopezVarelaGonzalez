from django.contrib import admin
from . models import Oferta,Producto,Comuna,Tienda,Region,Venta
# Register your models here.

admin.site.register(Oferta)
admin.site.register(Producto)
admin.site.register(Tienda)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Venta)