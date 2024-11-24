#urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

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
]
