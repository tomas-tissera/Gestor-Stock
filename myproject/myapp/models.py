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
    