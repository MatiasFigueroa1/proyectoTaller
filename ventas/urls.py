from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ventas_view, name='Ventas'),
    path('clientes/', views.clientes_view, name='Clientes'),
]

