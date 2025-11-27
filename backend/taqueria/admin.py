from django.contrib import admin
from .models import Categoria, Taco, Pedido, DetallePedido

# Configuración para ver los detalles dentro del pedido en el admin
class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha', 'total', 'estado')
    list_filter = ('estado', 'fecha')
    inlines = [DetallePedidoInline] # Permite ver qué tacos pidieron dentro del pedido

admin.site.register(Categoria)
admin.site.register(Taco)
admin.site.register(Pedido, PedidoAdmin)
# No registramos DetallePedido suelto porque ya está dentro de PedidoAdmin