from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('listar_proveedores/', views.listar_proveedores, name = "listar_proveedores"),
    path('listar_productos/', views.listar_productos, name = "listar_productos"),
    path('update_productos/<int:pk>', views.actualizar_producto, name = "update_productos"),
    path('update_proveedor/<int:pk>', views.actualizar_proveedor, name = "update_proveedor"),
    path('borrar_producto/<int:pk>', views.borrar_producto, name = "borrar_productos"),
    path('borrar_proveedor/<int:pk>', views.borrar_proveedor, name = "borrar_proveedor"),

]