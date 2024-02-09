from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Modelo para el tipo de café
class TipoCafe(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="cafe/imagenes/", blank=True)

    def __str__(self):
        return self.nombre

# Modelo para el tamaño del café
class TamanoCafe(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

# Modelo para el café
class Cafe(models.Model):
    tipo = models.ForeignKey(TipoCafe, on_delete=models.CASCADE)
    tamano = models.ForeignKey(TamanoCafe, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="cafe/imagenes/", blank=True)
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo} - {self.tamano}"

# Modelo para el cliente
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para la venta
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.ForeignKey('MetodoPago', on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta a {self.cliente} - {self.cafe}"

# Modelo para el inventario
class Inventario(models.Model):
    cafe = models.OneToOneField(Cafe, on_delete=models.CASCADE) # Cambiado a OneToOneField para relación única con el café
    stock = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Inventario de {self.cafe}"

# Modelo para las promociones
class Promocion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_promocion = models.CharField(max_length=255)
    condiciones = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

# Modelo para las imágenes de las promociones
class ImagenPromocion(models.Model):
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="promociones/imagenes/") # Añadido campo de imagen para las promociones

    def __str__(self):
        return f"Imagen de {self.promocion}"

# Modelo para el método de pago
class MetodoPago(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
