from django.contrib import admin
from .models import *
# Register your models here.
class Articulosadmin(admin.ModelAdmin):
    search_fields=('nombre_articulo',)
    list_filter=('categoria_articulo',)

admin.site.register(Articulos,Articulosadmin)

class Clientesadmin(admin.ModelAdmin):
    search_fields=('nombre_cliente',)
admin.site.register(Cliente,Clientesadmin)

class Pedidosadmin(admin.ModelAdmin):
    search_fields=('codigo_seguimiento',)
    list_filter=('fecha_pedido',)
    date_hierarchy=('fecha_pedido')
admin.site.register(Pedidos,Pedidosadmin)