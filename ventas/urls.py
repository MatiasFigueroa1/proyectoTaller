from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ventas_view, name='Ventas'),
    path('clientes/', views.clientes_view, name='Clientes'),
    path('add_clientes', views.add_cliente_view, name='AddCliente'),
    path('delete_clientes', views.delete_cliente_view, name='DeleteCliente'),
    path('credito/', views.credito, name='credito' )
]

