from django.contrib import admin
from .models import Empleado

# Register your models here.


@admin.register(Empleado)
class AdminEmpleado(admin.ModelAdmin):
    pass
