from django.contrib import admin
from .models import Categoria, Producto, Usuario, Pedido, DetallePedido, Pago, Despacho

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Pago)
admin.site.register(Despacho)
