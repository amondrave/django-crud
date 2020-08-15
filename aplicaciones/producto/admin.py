from django.contrib import admin
from .models import TipoProducto, Producto

# Register your models here.


@admin.register(TipoProducto)
class AdminTipoProducto(admin.ModelAdmin):
    pass


@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    pass
