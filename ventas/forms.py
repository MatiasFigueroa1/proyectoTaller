from django.db import models

class ClienteForm(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    rut = models.CharField(max_length=15, unique=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    credito = models.ForeignKey('Credito', on_delete=models.CASCADE, related_name='transacciones')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transacción de {self.monto} para {self.credito.cliente.nombre} el {self.fecha}"

class Credito(models.Model):
    cantCredito = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cliente = models.OneToOneField('Cliente', on_delete=models.CASCADE)

    def credito_utilizado(self):
        # Calcula el crédito utilizado
        return sum(transaccion.monto for transaccion in self.transacciones.all())

    def credito_disponible(self):
        # Calcula el crédito disponible restando el crédito utilizado al total del crédito
        if self.cantCredito is not None:
            return self.cantCredito - self.credito_utilizado()
        return None

    def __str__(self):
        # Muestra el crédito utilizado y el crédito disponible en el string de representación
        return f"{self.cliente.nombre} - Crédito Utilizado: {self.credito_utilizado()} - Crédito Disponible: {self.credito_disponible()}"
