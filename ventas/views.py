from django.shortcuts import render
from .models import Cliente
# Create your views here.
def ventas_view(request):
    num_ventas = 156
    context ={
        'num_ventas': num_ventas,
    }
    return render(request, 'ventas.html', context)

def clientes_view(request):
    clientes = Cliente.objects.all()
    context ={
        'clientes': clientes,
        
    }
    return render(request, 'clientes.html', context)