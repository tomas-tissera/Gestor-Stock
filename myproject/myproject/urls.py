from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),  # Redirige a la vista de login
    path('admin/', admin.site.urls),
    path('role-based/', views.role_based_view, name='role_based_view'),
]
