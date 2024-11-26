# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Empleados , Categoria, Producto , Cliente , Venta, DetalleVenta

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


# forms.py
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'vendedor', 'metodo_pago']  # Excluye 'fecha_venta'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['vendedor'].queryset = User.objects.filter(groups__name='Vendedores')  # Opcional: Filtrar a los usuarios del grupo 'Vendedores'

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio_unitario']