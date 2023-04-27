"""MealMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dietas/', views.listarDietas, name='listarDietas'),
    path('dietas/alimentos/<str:idDieta>/', views.listarAlimentos, name='DescripcionComidas'),
    path('modificarDieta/agregarDieta/<str:idDieta>/', views.agregarADieta, name="agregarADieta"),
    path('modificarDieta/agregarComida/<str:idComida>/<str:idDieta>/', views.agregarComida, name="agregarComida"),
    path('modificarDieta/eliminarDieta/<str:idDieta>/', views.eliminarAdieta, name="eliminarAdieta"),
    path('modificarDieta/eliminarComida/<str:idComida>/<str:idDieta>/', views.eliminarComida, name="eliminarComida"),
    path('rutinas/', views.listarRutinas, name='listarRutinas'),
    path('rutinas/ejercicios/<str:idRutina>/', views.listarEjercicios, name='DescripcionEjercicios'),
    path('modificarRutina/agregarRutina/<str:idRutina>/', views.agregarARutina, name="agregarARutina"),
    path('modificarRutina/agregarEjercicio/<str:idEjercicio>/<str:idRutina>/', views.agregarEjercicio, name="agregarEjercicio"),
    path('modificarRutina/eliminarRutina/<str:idRutina>/', views.eliminarARutina, name="eliminarARutina"),
    path('modificarRutina/eliminarEjercicio/<str:idEjercicio>/<str:idRutina>/', views.eliminarEjercicio, name="eliminarEjercicio"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name='registro')
] 
