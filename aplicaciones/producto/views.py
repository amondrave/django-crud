from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm, TipoProductoForm
from .models import Producto, TipoProducto

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


@method_decorator(login_required, name='dispatch')
class CrearProductoView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/crear_producto.html'
    success_url = reverse_lazy('producto:listar_producto')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo': 'crear producto',
                                                    'form': self.form_class})


@method_decorator(login_required, name='dispatch')
class EliminarProductoView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto:listar_producto')


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


@method_decorator(login_required, name='dispatch')
class EditarProductoView(UpdateView):
    model = Producto
    template_name = 'producto/editar_producto.html'
    # Se utiliza un formulario para que se envie al template
    form_class = ProductoForm
    # Se define la accion que el va a realizar una vez haga el proceso
    success_url = reverse_lazy('producto:listar_producto')


class CrearTipoView(CreateView):
    tipo = TipoProducto
    form_class = TipoProductoForm
    template_name = 'producto/crear_tipo.html'
    success_url = reverse_lazy('index')
