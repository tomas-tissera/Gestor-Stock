from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.home_view, name='login'),  # Vista para la raíz
    path('role-based/', views.role_based_view, name='role_based_view'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Aquí debe ser 'logout'

]
