from django.contrib import admin
from pedidos.models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["nombre_cliente","numero_telefonico",'direccion','observacion','productos','estado','fecha','metodo_pago','total']