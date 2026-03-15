from django.contrib import admin
from django.urls import path
from usuarios.views import lista_usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', lista_usuarios),
]