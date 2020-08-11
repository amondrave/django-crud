from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
from .models import Producto

# Create your views here.

"""
Vamos a migrar las vistas basadas en funciones por vistas basadas
en clase para aprovechar al maximo lo que el framework nos ofrece

"""

# Vista basada en el template view para renderizar el template con el
# contexto de la vista


@method_decorator(login_required, name='dispatch')
class InicioView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo': 'bienvenidos'})


@login_required()
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

# Vista basa en ListView para mostrar informacion de la base de datos
# en templates


@method_decorator(login_required, name='dispatch')
class ListarProductoView(ListView):
    model = Producto  # Modelo de la base de datos
    template_name = 'producto/listar_producto.html'
    queryset = Producto.objects.all()  # Consulta que vamos a hacer
    # Nombre del contexto que queremos dar
    context_object_name = 'productos'


# eliminación directa

@login_required()
def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect('producto:listar_producto')


@login_required()
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
