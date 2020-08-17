"""almacen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicaciones.producto.views import InicioView
from aplicaciones.usuario.views import LoginView, cerrar_sesion, EmpleadoCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', InicioView.as_view(), name='index'),
    path('producto/', include(('aplicaciones.producto.urls', 'producto'))),
    path('', LoginView.as_view(), name='login'),
    path('logout', cerrar_sesion, name='logout'),
    path('registro', EmpleadoCreateView.as_view(), name='registro')
]
