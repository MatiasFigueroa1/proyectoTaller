from django.contrib import admin
from ventas.models import Cliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display= ('nombre','rut')
    search_fields = ['nombre']
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)
