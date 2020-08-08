from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProductoForm
from .models import Producto

# Create your views here.


def inicio(request):
    return render(request, 'index.html', {'titulo': 'Bienvenidos'})


def crear_producto(request):
    titulo = 'crear productos'
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('index')
    else:
        producto_form = ProductoForm
        return render(request, 'producto/crear_producto.html', {'producto_form': producto_form, 'titulo': titulo})


def listar_producto(request):
    titulo = 'Productos'
    productos = Producto.objects.all()
    return render(request, 'producto/listar_producto.html', {'productos': productos, 'titulo': titulo})

# eliminación directa


def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect('producto:listar_producto')


def editar_producto(request, codigo):
    producto_form = None
    error = None
    try:
        producto = Producto.objects.get(codigo=codigo)
        if request.method == 'GET':
            # usamos get para traer la informacion del producto
            # si esto es asi volvemos a usar el formulario para crear productos
            # la instancia es para que me traiga el formulario con los datos que
            # tiene el objeto que vamos a editar
            producto_form = ProductoForm(instance=producto)
        else:
            # Cuando ya hayamos modificado los cambios debemos guardar en la base
            # para eso creamos el formulario pero con POST y con la instancia del objeto
            producto_form = ProductoForm(request.POST, instance=producto)
            if producto_form.is_valid():
                # si el producto es valido aplicamos los cambios
                producto_form.save()
                return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'producto/editar_producto.html', {
        'producto_form': producto_form,
        'titulo': 'editar producto',
        'error': error
    })
