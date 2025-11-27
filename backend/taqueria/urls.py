from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:taco_id>/', views.agregar_al_carrito, name='agregar_carrito'),
    path('eliminar/<int:taco_id>/', views.eliminar_del_carrito, name='eliminar_carrito'),
    path('procesar/', views.procesar_pedido, name='procesar_pedido'),
    path('mis-pedidos/', views.historial_pedidos, name='historial_pedidos'),
]