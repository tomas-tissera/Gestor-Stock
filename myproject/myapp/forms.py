# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Empleados , Categoria, Producto , Cliente , Venta, DetalleVenta
from django.core.exceptions import ValidationError

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['nombre', 'apellido', 'telefono', 'email', 'rol']

    # Si quieres asociar el User de forma automática en el formulario, puedes hacerlo aquí:
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = User.objects.create_user(username=self.cleaned_data['email'], email=self.cleaned_data['email'], password='default_password')
        if commit:
            instance.save()
        return instance

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'descripcion', 'precio', 'cantidad', 'categoria']
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'compania', 'email', 'telefono', 'direccion', 'estatus', 'notas']



class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'vendedor', 'metodo_pago']

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio_unitario']

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')

        if producto and cantidad:
            if producto.cantidad < cantidad:
                raise ValidationError(
                    f"No hay suficiente stock para el producto {producto.titulo}. (Stock disponible: {producto.cantidad})"
                )

        return cleaned_data
