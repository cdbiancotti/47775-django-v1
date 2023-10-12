"""
URL configuration for primerdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from primerdjango.views import mi_vista, otra_vista, saludo, mi_primer_template
from inicio.views import crear_auto

urlpatterns = [
    path('', mi_vista),
    path('fecha/', otra_vista),
    path('saludo/<str:nombre_completo>/', saludo),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo),
    path('mi-primer-template/', mi_primer_template),
    path('crear-auto/<str:marca>/<str:modelo>/<int:anio>/', crear_auto),
    path('admin/', admin.site.urls),
]
