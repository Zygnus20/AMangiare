from django.db import models

estados_pedidos = (
    ("ABIERTO", "Abierto"),
    ("CANCELADO", "Cancelado"),
    ("CERRADO", "Cerrado"),
)
tipo_pago = (
    ("TRANSFERENCIA", "Transferencia"),
    ("EFECTIVO", "Efectivo"),
    ("DÉBITO/CRÉDITO", "Débito/Crédito"),
)


class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=255)
    numero_telefonico = models.IntegerField()
    direccion = models.CharField(max_length=255)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    productos = models.ForeignKey("productos.Producto", on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(max_length=255, choices=estados_pedidos)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=255, choices=tipo_pago)
    total = models.IntegerField()

    def __str__(self):
        return self.nombre_cliente