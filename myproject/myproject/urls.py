from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('accounts/profile/', lambda request: redirect('/')),  # Redirige a la página principal
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
