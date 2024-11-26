from django.contrib import admin
from .models import Categoria, Producto, Cliente, Venta

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'precio', 'cantidad', 'categoria', 'fecha_creacion')
    list_filter = ('categoria', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'estatus', 'fecha_registro')
    search_fields = ('nombre', 'email', 'telefono')

@admin.register(Venta)  # Registra el modelo Venta
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'vendedor', 'fecha_venta', 'total_venta')
    list_filter = ('fecha_venta', 'vendedor')
    search_fields = ('cliente__nombre', 'vendedor__username', 'total_venta')
