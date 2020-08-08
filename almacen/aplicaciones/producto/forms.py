from django import forms as fm
from .models import TipoProducto, Producto

# Formulario del tipo de producto


class TipoProductoForm(fm.ModelForm):
    # metadatos que tendra nuestro formulario
    class Meta:
        model = TipoProducto
        fields = ['nombre']

# Formlario del producto


class ProductoForm(fm.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'tipo']
