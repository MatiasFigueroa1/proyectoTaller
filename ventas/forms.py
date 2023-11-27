from django import forms
from .models import Cliente, Credito

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'rut']
        labels = {
            'nombre': 'Nombre cliente: ',
            'rut': 'Rut cliente: '
        }

class AddCreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = ['cantCredito']
        labels = {
            'cantCredito': 'Cantidad de Crédito: '
        }
