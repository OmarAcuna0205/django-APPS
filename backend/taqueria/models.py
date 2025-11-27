from django.db import models
from django.contrib.auth.models import User

# 1. Modelo para Categorías (ej. Tacos, Bebidas, Postres)
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# 2. Modelo para los Tacos (Productos) 
class Taco(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # El campo de imagen es opcional como pide el examen
    imagen = models.ImageField(upload_to='tacos/', null=True, blank=True) 

    def __str__(self):
        return self.nombre

# 3. Modelo de Pedido (Incluye tu Opción A: Estados) [cite: 46]
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('preparacion', 'En Preparación'),
        ('entregado', 'Entregado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    # Aquí está tu toque personal:
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Pedido {self.id} de {self.usuario.username} ({self.estado})"

# 4. Detalle del Pedido (Relación Muchos a Muchos intermedia) 
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    taco = models.ForeignKey(Taco, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculamos el subtotal automáticamente antes de guardar
        self.subtotal = self.taco.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.taco.nombre}"