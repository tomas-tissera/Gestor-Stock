#views.py
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Count, Sum

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirige a usuarios autenticados

def role_based_view(request):
    # Calcular totales
    total_clientes = Cliente.objects.count()
    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    
    # Calcular total de ventas
    total_ventas = Venta.objects.aggregate(Sum('total_venta'))['total_venta__sum'] or 0
    total_ventas = round(total_ventas, 2)  # Redondear a dos decimales

    # Calcular ventas por método de pago
    ventas_por_metodo = Venta.objects.values('metodo_pago').annotate(total=Sum('total_venta'))

    # Calcular ventas por vendedor
    ventas_por_vendedor = Venta.objects.values('vendedor__username').annotate(total_ventas=Sum('total_venta')).order_by('-total_ventas')

    # Calcular datos para gráficos de categorías
    categorias_chart_data = Categoria.objects.annotate(total_ventas=Sum('productos__venta__total_venta'))

    context = {
        'total_clientes': total_clientes,
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'total_ventas': total_ventas,
        'ventas_por_metodo': ventas_por_metodo,
        'ventas_por_vendedor': ventas_por_vendedor,
        'categorias_chart_data': categorias_chart_data,
        'role': 'Empleados' if request.user.groups.filter(name='Empleados').exists() else 'Encargado',  # Suponiendo que tienes grupos para roles
        'user': request.user
    }

    return render(request, 'role_based_template.html', context)

def home_view(request):
    return render(request, 'home.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('role_based_view')  # Redirige a 'role_based_view' después de iniciar sesión

#Gestion de empleados
def gestion_empleados(request):
    # Filtrar los empleados que están en el grupo 'Empleados'
    empleados = Empleados.objects.all()

    return render(request, 'empleados/empleados_gestion.html', {'empleados': empleados})

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
    return render(request, 'empleados/empleado_form.html', {'form': form})
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
    template_name = "categorias/categoria_list.html"
    context_object_name = "categorias"

    def get_queryset(self):
        # Obtener el término de búsqueda desde la URL (GET)
        search_query = self.request.GET.get('q', '')

        if search_query:
            # Filtrar las categorías que contengan el término de búsqueda en su nombre
            return Categoria.objects.filter(nombre__icontains=search_query)
        else:
            # Si no hay búsqueda, retornar todas las categorías
            return Categoria.objects.all()
# Detalle de una categoría (opcional)
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "categorias/categoria_detail.html"
    context_object_name = "categoria"

# Crear categoría
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = "categorias/categoria_form.html"
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('categoria_list')

# Editar categoría
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = "categorias/categoria_form.html"
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('categoria_list')

# Eliminar categoría
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "categorias/categoria_confirm_delete.html"
    success_url = reverse_lazy('categoria_list')

# Listar productos
class ProductoListView(ListView):
    model = Producto
    template_name = "productos/producto_list.html"
    context_object_name = "productos"

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener el parámetro de búsqueda desde la URL
        query = self.request.GET.get('q')

        # Si hay un término de búsqueda, filtrar los productos por el nombre (titulo)
        if query:
            queryset = queryset.filter(titulo__icontains=query)  # Filtra productos cuyo título contenga la cadena

        return queryset
# Detalle de un producto
class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/producto_detail.html"
    context_object_name = "producto"

# Crear producto
class ProductoCreateView(CreateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ['titulo', 'descripcion', 'precio', 'cantidad', 'categoria']
    success_url = reverse_lazy('producto_list')

# Editar producto
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ['titulo', 'descripcion', 'precio', 'cantidad', 'categoria']
    success_url = reverse_lazy('producto_list')

# Eliminar producto
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy('producto_list')

# Listar clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/cliente_list.html"
    context_object_name = "clientes"
    
# Detalle de un producto
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "clientes/cliente_detail.html"
    context_object_name = "producto"

# Crear producto
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "clientes/cliente_form.html"
    fields = ['nombre', 'compania', 'email', 'telefono', 'direccion', 'estatus', 'notas']
    success_url = reverse_lazy('clientes_list')

# Editar producto
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "clientes/cliente_form.html"
    fields = ['nombre', 'compania', 'email', 'telefono', 'direccion', 'estatus', 'notas']
    success_url = reverse_lazy('clientes_list')

# Eliminar producto
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "clientes/cliente_confirm_delete.html"
    success_url = reverse_lazy('clientes_list')

#views.py
#Venta
# Listar todas las ventas
class VentaListView(ListView):
    model = Venta
    template_name = 'ventas/venta_list.html'
    context_object_name = 'ventas'

    def get_queryset(self):
        return Venta.objects.all()  # Asegúrate de que las ventas tengan un vendedor asignado

# Detalle de una venta
# views.py
class VentaDetailView(DetailView):
    model = Venta
    template_name = 'ventas/venta_detail.html'
    context_object_name = 'venta'

# Crear nueva venta con productos
class VentaCreateView(CreateView):
    model = Venta
    template_name = 'ventas/venta_form.html'
    form_class = VentaForm
    success_url = reverse_lazy('venta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos_en_stock = Producto.objects.filter(cantidad__gt=0)
        context['productos'] = productos_en_stock
        return context

    def form_valid(self, form):
        venta = form.save()
        productos = []
        cantidades = []
        precios = []

        # Procesar dinámicamente los campos del formulario
        for key, value in self.request.POST.items():
            if key.startswith('producto_'):
                productos.append(value)
            elif key.startswith('cantidad_'):
                cantidades.append(value)
            elif key.startswith('precio_unitario_'):
                precios.append(value)

        for producto_id, cantidad, precio in zip(productos, cantidades, precios):
            if producto_id:  # Validar que el producto haya sido seleccionado
                producto = Producto.objects.get(id=producto_id)
                detalle = DetalleVenta(
                    venta=venta,
                    producto=producto,
                    cantidad=int(cantidad),
                    precio_unitario=float(precio),
                )
                detalle.save()

        venta.calcular_total()
        return redirect(self.success_url)

class VentaUpdateView(UpdateView):
    model = Venta
    template_name = 'ventas/venta_form.html'
    form_class = VentaForm
    success_url = reverse_lazy('venta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener la venta que estamos editando
        venta = self.get_object()
        # Obtener los detalles de esa venta
        detalles = DetalleVenta.objects.filter(venta=venta)
        context['detalles'] = detalles
        return context

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'ventas/venta_confirm_delete.html'
    success_url = reverse_lazy('venta_list')

# Crear detalle de venta
class DetalleVentaCreateView(CreateView):
    model = DetalleVenta
    template_name = 'ventas/detalle_venta_form.html'
    fields = ['venta', 'producto', 'cantidad', 'precio_unitario']
    success_url = reverse_lazy('venta_list')

    def form_valid(self, form):
        if not form.is_valid():
            # Imprimir los errores del formulario si no es válido
            print(form.errors)
            return self.form_invalid(form)

        # Guardar la venta
        venta = form.save()

        # Asegúrate de que la venta se ha guardado correctamente
        if not venta:
            form.add_error(None, "No se pudo guardar la venta.")
            return self.form_invalid(form)

        # Procesar los productos, cantidades y precios
        productos = []
        cantidades = []
        precios = []

        for key, value in self.request.POST.items():
            if key.startswith('producto_'):
                productos.append(value)
            elif key.startswith('cantidad_'):
                cantidades.append(value)
            elif key.startswith('precio_unitario_'):
                precios.append(value)

        try:
            # Guardar los detalles de la venta
            for producto_id, cantidad, precio in zip(productos, cantidades, precios):
                if producto_id:
                    producto = Producto.objects.get(id=producto_id)
                    if producto.cantidad >= int(cantidad):
                        detalle = DetalleVenta(
                            venta=venta,
                            producto=producto,
                            cantidad=int(cantidad),
                            precio_unitario=float(precio),
                        )
                        detalle.save()

                        # Actualizar el stock del producto
                        producto.actualizar_stock(int(cantidad))
                    else:
                        form.add_error(None, f"No hay suficiente stock para el producto: {producto.titulo}")
                        return self.form_invalid(form)

            # Calcular el total de la venta
            venta.calcular_total()

        except ValueError as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)

        return redirect(self.success_url)
