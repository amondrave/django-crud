from django import forms as fm
from .models import TipoProducto, Producto

# Formulario del tipo de producto


class TipoProductoForm(fm.ModelForm):
    # metadatos que tendra nuestro formulario
    class Meta:
        model = TipoProducto
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre del nuevo tipo'
        }
        widgets = {
            'nombre': fm.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del tipo de producto'
                }
            )
        }

# Formlario del producto


class ProductoForm(fm.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'tipo']
        labels = {
            'codigo': 'codigo del producto',
            'nombre': 'nombre del producto',
            'tipo': 'tipo del producto',
        }
        widgets = {
            'codigo': fm.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el codigo del producto'
                }
            ),
            'nombre': fm.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),
            'tipo': fm.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
