#views.py
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Empleados , Producto, Categoria
from .forms import EmpleadoForm  # Asegúrate de que tienes un formulario para crear empleados
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import EmpleadoForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirige a usuarios autenticados


@login_required
def role_based_view(request):
    user = request.user

    # Verifica si el usuario pertenece al grupo 'Encargado' o 'Empleados'
    if user.groups.filter(name='Encargado').exists():
        role = 'Encargado'
    elif user.groups.filter(name='Empleados').exists():
        role = 'Empleados'
    else:
        role = 'Invitado'  # Si el usuario no tiene rol asignado

    return render(request, 'role_based_template.html', {'role': role})

def home_view(request):
    return render(request, 'home.html')
@login_required
def role_based_view(request):
    user = request.user

    # Verifica si el usuario pertenece al grupo 'Encargado' o 'Empleados'
    if user.groups.filter(name='Encargado').exists():
        role = 'Encargado'
    elif user.groups.filter(name='Empleados').exists():
        role = 'Empleados'
    else:
        role = 'Invitado'

    return render(request, 'role_based_template.html', {'role': role})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('role_based_view')  # Redirige a 'role_based_view' después de iniciar sesión

#Gestion de empleados
def gestion_empleados(request):
    # Filtrar los empleados que están en el grupo 'Empleados'
    empleados = Empleados.objects.all()

    return render(request, 'empleados_gestion.html', {'empleados': empleados})


@login_required
def crear_empleado(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        rol = request.POST.get('rol')

        # Crear el nuevo usuario (solo si no existe ya)
        user = User.objects.create_user(username=email, email=email, password='temp_password')  # O usa otro campo como username

        # Crear el nuevo empleado
        empleado = Empleados.objects.create(
            user=user,  # Asocia el usuario
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email,
            rol=rol
        )

        return redirect('gestion_empleados')  # Redirige a la vista de gestión de empleados después de crear el empleado

    return render(request, 'empleados/crear_empleado.html')

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleados, id=id)  # Obtener el empleado por ID
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)  # Cargar los datos del empleado en el formulario
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('gestion_empleados')  # Redirigir a la vista de gestión de empleados
    else:
        form = EmpleadoForm(instance=empleado)  # Prellenar el formulario con los datos del empleado
    return render(request, 'empleado_form.html', {'form': form})
# Vista para eliminar un empleado
def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleados, id=id)  # Obtén el empleado por ID
    if request.method == 'POST':  # Solo permite eliminar si es una solicitud POST
        empleado.delete()  # Elimina el empleado
        return redirect('gestion_empleados')  # Redirige a la vista de gestión de empleados
    return render(request, 'confirmar_eliminacion.html', {'empleado': empleado})

# Listar categorías
class CategoriaListView(ListView):
    model = Categoria
    template_name = "categoria_list.html"
    context_object_name = "categorias"

# Detalle de una categoría (opcional)
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "categoria_detail.html"
    context_object_name = "categoria"

# Crear categoría
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = "categoria_form.html"
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('categoria_list')

# Editar categoría
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = "categoria_form.html"
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('categoria_list')

# Eliminar categoría
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "categoria_confirm_delete.html"
    success_url = reverse_lazy('categoria_list')

# Listar productos
class ProductoListView(ListView):
    model = Producto
    template_name = "producto_list.html"
    context_object_name = "productos"

# Detalle de un producto
class ProductoDetailView(DetailView):
    model = Producto
    template_name = "producto_detail.html"
    context_object_name = "producto"

# Crear producto
class ProductoCreateView(CreateView):
    model = Producto
    template_name = "producto_form.html"
    fields = ['titulo', 'descripcion', 'precio', 'cantidad', 'categoria']
    success_url = reverse_lazy('producto_list')

# Editar producto
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "producto_form.html"
    fields = ['titulo', 'descripcion', 'precio', 'cantidad', 'categoria']
    success_url = reverse_lazy('producto_list')

# Eliminar producto
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "producto_confirm_delete.html"
    success_url = reverse_lazy('producto_list')