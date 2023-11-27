from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    rut = models.CharField(max_length=15, unique=True, blank=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre

class Credito(models.Model):
    cantCredito = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cliente = models.OneToOneField('Cliente', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente.nombre} - Credito: {self.cantCredito}"
