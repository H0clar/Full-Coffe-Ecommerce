

from django.contrib import admin
from .models import TipoCafe, TamanoCafe, Cafe, Cliente, Venta, Inventario, Promocion, ImagenPromocion, MetodoPago

# Register your models here.

class TipoCafeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'imagen')

class TamanoCafeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio_base')

class CafeAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'tamano', 'precio', 'descripcion', 'imagen', 'stock', 'disponible')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellido', 'correo_electronico', 'telefono', 'direccion', 'fecha_nacimiento')

class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cafe', 'fecha_venta', 'cantidad', 'precio_unitario', 'total', 'impuesto', 'metodo_pago')

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('cafe', 'stock')

class PromocionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_inicio', 'fecha_fin')

class ImagenPromocionAdmin(admin.ModelAdmin):
    list_display = ('promocion', 'imagen')

class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

admin.site.register(TipoCafe, TipoCafeAdmin)

admin.site.register(TamanoCafe, TamanoCafeAdmin)

admin.site.register(Cafe, CafeAdmin)

admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Venta, VentaAdmin)

admin.site.register(Inventario, InventarioAdmin)

admin.site.register(Promocion, PromocionAdmin)

admin.site.register(ImagenPromocion, ImagenPromocionAdmin)

admin.site.register(MetodoPago, MetodoPagoAdmin)

