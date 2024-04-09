from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm

#Crear proveedor
def agregar_proveedor(request):
    form = ProveedorForm()
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'agregar_proveedor.html', {'form': form})


#Crear producto
def agregar_producto(request):
    form = ProductoForm(proveedor_choices=Proveedor.objects.all())
    if request.method == 'POST':
        form = ProductoForm(request.POST, proveedor_choices=Proveedor.objects.all())
        if form.is_valid():
            form.save()
    return render(request, 'agregar_producto.html', {'form': form, 'proveedores': Proveedor.objects.all()})

#Listar todos los proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

#Listar todos los productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

#Actualizar Producto
def actualizar_producto(request, id, nombre, precio, stock):
    producto = Producto.objects.get(id = id)
    producto.nombre = nombre
    producto.precio = precio
    producto.stock = stock
    producto.save()
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

#Actualizar Proveedor
def actualizar_proveedor(request, id, nombre, apellido, dni):
    proveedor = Proveedor.objects.get(id = id)
    proveedor.nombre = nombre
    proveedor.apellido = apellido
    proveedor.dni = dni
    proveedor.save()
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

#Borrar producto
def borrar_producto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})