# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Empleados

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
