from django.shortcuts import render
from .models import Oferta,Producto,Tienda,Venta
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DateDetailView,ListView
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

def index(request):
    num_producto = Producto.objects.all()
    return render(
        request,
        'index.html',
        context={'num_producto':num_producto},
    )
    
def contacto(request):
    return render(
        request,
        'contacto.html',
    )

## Clases para Producto

class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['precio','nombre','descripcion','oferta','tienda']

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('index')

class ProductoDetailView(generic.DetailView):
    model = Producto

class ProductoListView(ListView):
    model = Producto

## Clases para los Oferta

class OfertaCreate(CreateView):
    model = Oferta
    fields = '__all__'

class OfertaUpdate(UpdateView):
    model = Oferta
    fields = ['oferta','detalle','fecha_oferta']

class OfertaDelete(DeleteView):
    model = Oferta
    success_url = reverse_lazy('index')

class OfertaDetailView(generic.DetailView):
    model = Oferta

class OfertaListView(ListView):
    model = Oferta

## Clases para Tienda

class TiendaCreate(CreateView):
    model = Tienda
    fields = '__all__'

class TiendaUpdate(UpdateView):
    model = Tienda
    fields = ['nombre','correo','direccion','comuna']

class TiendaDelete(DeleteView):
    model = Tienda
    success_url = reverse_lazy('index')

class TiendaDetailView(generic.DetailView):
    model = Tienda

class TiendaListView(ListView):
    model = Tienda

## Clases para Venta

class VentaCreate(CreateView):
    model = Venta
    fields = '__all__'

class VentaUpdate(UpdateView):
    model = Venta
    fields = ['fecha_venta','producto','oferta','tienda']

class VentaDelete(DeleteView):
    model = Venta
    success_url = reverse_lazy('index')

class VentaDetailView(generic.DetailView):
    model = Venta

class VentaListView(ListView):
    model = Venta