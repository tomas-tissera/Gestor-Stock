#urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    
    path('', CustomLoginView.as_view(), name='login'),  # Cambia a CustomLoginView
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('role-based/', views.role_based_view, name='role_based_view'),
    
    #url gestion de empleados
    path('gestion_empleados/', views.gestion_empleados, name='gestion_empleados'),
    path('gestion_empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('gestion_empleados/editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('gestion_empleados/eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('gestion_empleados/crear/', views.crear_empleado, name='crear_empleado'),

    #url gestion de Productos
    # Categorías
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nueva/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),

    # Productos
    path('productos/', views.ProductoListView.as_view(), name='producto_list'),
    path('productos/nuevo/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_delete'),

    # Clientes
    path('clientes/', views.ClienteListView.as_view(), name='clientes_list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='clientes_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='clientes_update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='clientes_delete'),


    # Ventas
    path('ventas/', VentaListView.as_view(), name='venta_list'),
    path('ventas/<int:pk>/', VentaDetailView.as_view(), name='venta_detail'),
    path('ventas/nuevo/', VentaCreateView.as_view(), name='venta_create'),
    path('ventas/<int:pk>/editar/', VentaUpdateView.as_view(), name='venta_edit'),
    path('ventas/<int:pk>/eliminar/', VentaDeleteView.as_view(), name='venta_delete'),
]
