from django.shortcuts import render, redirect
from .models import Cliente, Credito
from .forms import AddClienteForm, AddCreditoForm
from django.contrib import messages

def ventas_view(request):
    num_ventas = 156
    context = {
        'num_ventas': num_ventas,
    }
    return render(request, 'venta.html', context)

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()

    context = {
        'clientes': clientes,
        'form_personal': form_personal,
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages.error(request, "Error al guardar el cliente")
                return redirect('Clientes')
    return redirect('Clientes')

def delete_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect('Clientes')

def credito(request):
    if request.method == 'POST':
        form_cliente = AddClienteForm(request.POST)
        form_credito = AddCreditoForm(request.POST)

        if form_cliente.is_valid() and form_credito.is_valid():
            # Guardar el cliente
            cliente = form_cliente.save()
            
            credito = form_credito.save(commit=False)
            credito.cliente = cliente
            credito.save()
            
            messages.success(request, "Cliente y crédito guardados exitosamente.")
            return redirect('Clientes') 

    else:
        form_cliente = AddClienteForm()
        form_credito = AddCreditoForm()

    context = {
        'form_cliente': form_cliente,
        'form_credito': form_credito,
    }

    return render(request, 'credito.html', context)  # Cambia a la plantilla adecuada
