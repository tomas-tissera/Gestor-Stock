from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Vista para la raíz
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('role-based/', views.role_based_view, name='role_based_view'),
]
