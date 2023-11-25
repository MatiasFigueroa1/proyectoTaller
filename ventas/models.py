from django.db import models

# Create your models here.
class Cliente(models.Model):

    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=15, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
       return self.nombre

    