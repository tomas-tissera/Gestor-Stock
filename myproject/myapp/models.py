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
