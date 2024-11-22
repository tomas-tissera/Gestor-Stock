#urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.home_view, name='login'),  # Vista para la raíz
    path('role-based/', views.role_based_view, name='role_based_view'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Aquí debe ser 'logout'
    
    #url gestion de empleados
    path('gestion_empleados/', views.gestion_empleados, name='gestion_empleados'),
    path('gestion_empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('gestion_empleados/editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('gestion_empleados/eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    

]
