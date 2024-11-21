from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='login'),  # Vista para la raíz
    path('role-based/', views.role_based_view, name='role_based_view'),
]
