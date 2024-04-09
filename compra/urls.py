from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('listar_proveedores/', views.listar_proveedores, name = "Mostrar todos los proveedores"),
    path('listar_productos/', views.listar_productos, name = "listar_productos"),
    path('update_productos/<int:id>/<str:nombre>/<int:precio>/<int:stock>/', views.actualizar_producto, name = "update_productos"),
    path('update_proveedor/<int:id>/<str:nombre>/<str:apellido>/<int:dni>/', views.actualizar_proveedor, name = "update_proveedor"),

]