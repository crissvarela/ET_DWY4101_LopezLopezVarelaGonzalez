from django.urls import path
from . import views

urlpatterns=[ 
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
]

urlpatterns+=[
    path('venta/<int:pk>/',views.ProductoDetailView.as_view(), name='producto_detail'),
    path('oferta/<int:pk>/',views.OfertaDetailView.as_view(), name='oferta_detail'),
    path('tienda/<int:pk>/',views.TiendaDetailView.as_view(), name='tienda_detail'),
    path('venta/<int:pk>/',views.VentaDetailView.as_view(), name='venta_detail'),
    path('venta/', views.ProductoListView.as_view(), name='producto_list'),
    path('oferta/', views.OfertaListView.as_view(), name='oferta_list'),
    path('tienda/', views.TiendaListView.as_view(), name='tienda_list'),
    path('venta/', views.VentaListView.as_view(), name='venta_list'),
    path('venta/create/', views.ProductoCreate.as_view(), name='producto_create'),
    path('venta/update/<int:pk>/', views.ProductoUpdate.as_view(), name='producto_update'),
    path('venta/delete/<int:pk>/', views.ProductoDelete.as_view(), name='producto_delete'),
    path('oferta/create/', views.OfertaCreate.as_view(), name='oferta_create'),
    path('oferta/update/<int:pk>/', views.OfertaUpdate.as_view(), name='oferta_update'),
    path('oferta/delete/<int:pk>/', views.OfertaDelete.as_view(), name='oferta_delete'),
    path('tienda/create/', views.TiendaCreate.as_view(), name='tienda_create'),
    path('tienda/update/<int:pk>/', views.TiendaUpdate.as_view(), name='tienda_update'),
    path('tienda/delete/<int:pk>/', views.TiendaDelete.as_view(), name='tienda_delete'),
    path('venta/create/', views.VentaCreate.as_view(), name='venta_create'),
    path('venta/update/<int:pk>/', views.VentaUpdate.as_view(), name='venta_update'),
    path('venta/delete/<int:pk>/', views.VentaDelete.as_view(), name='venta_delete'),
]