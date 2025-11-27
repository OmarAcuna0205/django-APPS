from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Taco, Categoria, Pedido, DetallePedido
from django.contrib.auth import logout
from rest_framework import generics
from .serializers import TacoSerializer

# 1. Vista del Menú Principal
def menu_view(request):
    categorias = Categoria.objects.all()
    # Obtenemos todos los tacos, o filtramos si hay una categoría seleccionada
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        tacos = Taco.objects.filter(categoria_id=categoria_id)
    else:
        tacos = Taco.objects.all()
        
    return render(request, 'taqueria/menu.html', {
        'categorias': categorias,
        'tacos': tacos
    })

# 2. Agregar al Carrito (Usa sesiones de navegador)
def agregar_al_carrito(request, taco_id):
    carrito = request.session.get('carrito', {})
    taco = get_object_or_404(Taco, pk=taco_id)
    
    # Si el taco ya está, sumamos 1, si no, lo creamos
    if str(taco_id) in carrito:
        carrito[str(taco_id)]['cantidad'] += 1
    else:
        carrito[str(taco_id)] = {
            'nombre': taco.nombre,
            'precio': float(taco.precio),
            'cantidad': 1,
            'imagen': taco.imagen.url if taco.imagen else ''
        }
    
    request.session['carrito'] = carrito
    messages.success(request, f"¡{taco.nombre} agregado al carrito!")
    return redirect('menu')

# 3. Ver el Carrito
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'taqueria/carrito.html', {'carrito': carrito, 'total': total})

# 4. Eliminar del Carrito
def eliminar_del_carrito(request, taco_id):
    carrito = request.session.get('carrito', {})
    if str(taco_id) in carrito:
        del carrito[str(taco_id)]
        request.session['carrito'] = carrito
    return redirect('ver_carrito')

# 5. Procesar Pedido (Requiere estar logueado)
@login_required
def procesar_pedido(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('menu')

    # Calcular total total
    total_pedido = sum(item['precio'] * item['cantidad'] for item in carrito.values())

    # Crear el Pedido (Encabezado)
    pedido = Pedido.objects.create(
        usuario=request.user,
        total=total_pedido,
        estado='pendiente' # Tu toque personal (Opción A)
    )

    # Crear los Detalles (Renglones del pedido)
    for taco_id, item in carrito.items():
        taco = Taco.objects.get(id=taco_id)
        DetallePedido.objects.create(
            pedido=pedido,
            taco=taco,
            cantidad=item['cantidad'],
            subtotal=item['precio'] * item['cantidad']
        )

    # Limpiar carrito y avisar
    request.session['carrito'] = {}
    messages.success(request, f"¡Pedido #{pedido.id} confirmado con éxito!")
    return redirect('historial_pedidos')

def logout_view(request):
    logout(request)
    messages.success(request, "¡Sesión cerrada exitosamente!")
    return redirect('menu')

# 6. Historial de Pedidos (Toque Personal y Requisito)
@login_required
def historial_pedidos(request):
    # Traemos los pedidos del usuario ordenados del más nuevo al más viejo
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'taqueria/historial.html', {'pedidos': pedidos})

class TacoListAPI(generics.ListAPIView):
    queryset = Taco.objects.all()
    serializer_class = TacoSerializer