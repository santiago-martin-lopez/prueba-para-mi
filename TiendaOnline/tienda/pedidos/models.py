from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_cliente=models.CharField(max_length=100)
    email_cliente=models.EmailField()
    telefono_cliente=models.IntegerField()
    direccion_cliente=models.CharField(max_length=100)

    def __str__(self):
        super().__str__()
        return (f'cliente con el nombre {self.nombre_cliente}')

class Articulos(models.Model):
    nombre_articulo=models.CharField(max_length=100)
    categoria_articulo=models.CharField(max_length=100)
    precio_articulo=models.IntegerField()

    def __str__(self):
        super().__str__()
        return(f'es un articulo de la tienda con nombre {self.nombre_articulo}')

class Pedidos(models.Model):
    fecha_pedido=models.DateField()
    entrega_pedido=models.BooleanField(default=False)
    codigo_seguimiento=models.CharField(max_length=100)

    def __str__(self) -> str:
        super().__str__()
        return (f'es un pedido con codigo de seguimiento {self.codigo_seguimiento}')

