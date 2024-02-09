from django.contrib import admin
from django.urls import path

from CoffeEcommerce import views

# Importamos todas las vistas de la aplicación





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('inicio/', views.index, name='inicio'),
    path('productos/', views.productos, name='productos'),

]
