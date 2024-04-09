from django.shortcuts import render, redirect, get_object_or_404
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

def actualizar_producto(request, pk):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        producto = Producto.objects.get(pk=pk)
        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        producto.save()

        productos = Producto.objects.all()
        return render(request, 'listar_productos.html', {'productos': productos})

    else:
        producto = Producto.objects.get(pk=pk)
        return render(request, 'actualizar_producto.html', {'producto': producto})

#Actualizar Proveedor
def actualizar_proveedor(request, pk):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')

        proveedor = Proveedor.objects.get(pk=pk)
        proveedor.nombre = nombre
        proveedor.apellido = apellido
        proveedor.dni = dni
        proveedor.save()

        proveedores = Proveedor.objects.all()
        return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

    else:
        proveedor = Proveedor.objects.get(pk=pk)
        return render(request, 'actualizar_proveedor.html', {'proveedor': proveedor})

#Borrar producto
def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
    return redirect('listar_productos')

#Borrar proveedor
def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
    return redirect('listar_proveedores')