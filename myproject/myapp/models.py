from django.db import models
from django.contrib.auth.models import User

class Empleados(models.Model):
    ROLES = [
        ('Empleados', 'Empleados'),
        ('Encargado', 'Encargado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='empleados')  # Relación con el modelo User
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=50, null=True, blank=True, default='Empleado') 


    class Meta:
        verbose_name = "Empleados"
        verbose_name_plural = "Empleados"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} ({self.rol})"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  # Nombre único para evitar duplicados
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional de la categoría

    def __str__(self):
        return self.nombre  # Representación del nombre en el panel de administración


class Producto(models.Model):
    titulo = models.CharField(max_length=200)  # Título del producto
    descripcion = models.TextField()  # Descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    cantidad = models.PositiveIntegerField()  # Cantidad disponible
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')  
    # Relación con la categoría (muchos productos pueden pertenecer a una categoría)

    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación del producto
    ultima_actualizacion = models.DateTimeField(auto_now=True)  # Fecha de última actualización del producto

    def __str__(self):
        return self.titulo  # Representación del título en el panel de administración
    def actualizar_stock(self, cantidad_vendida):
        """
        Actualiza el stock del producto restando la cantidad vendida.
        Si el stock es insuficiente, levanta un error.
        """
        if self.cantidad >= cantidad_vendida:
            self.cantidad -= cantidad_vendida
            self.save()
        else:
            raise ValueError("Stock insuficiente para completar la venta")
class Cliente(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre Completo')
    compania = models.CharField(max_length=255, blank=True, null=True, verbose_name='Compañía')
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    telefono = models.CharField(max_length=15, verbose_name='Número de Teléfono')
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    estatus = models.CharField(
        max_length=20, 
        choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], 
        default='activo', 
        verbose_name='Estatus'
    )
    notas = models.TextField(blank=True, null=True, verbose_name='Notas Adicionales')
    
    def __str__(self):
        return f'{self.nombre} - {self.email}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-fecha_registro']

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    metodo_pago = models.CharField(max_length=50)
    productos = models.ManyToManyField(Producto, through='DetalleVenta')

    def calcular_total(self):
        # Calculamos el total sumando los subtotales de cada DetalleVenta
        total = sum(detalle.subtotal for detalle in self.detalleventa_set.all())
        self.total_venta = total
        self.save()

    def __str__(self):
        return f"Venta {self.id} - Cliente: {self.cliente}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"Detalle Venta {self.id} - Producto: {self.producto} - Cantidad: {self.cantidad}"

