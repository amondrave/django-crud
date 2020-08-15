from django.db import models

# Create your models here.

# Modelo tipo de producto


class TipoProducto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=150, null=False, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.nombre)


# Modelo Producto
# este modelo debe tener una referencia hacia un tipo de producto

class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150, null=False, unique=True)
    fecha_creacion = models.DateField(
        'Fecha de creacion', auto_now=True, auto_now_add=False)
    # relacion uno a muchos
    # quiere decir que un tipo puede tener muchos productos y que un
    # producto solo puede tener un tipo
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return "codigo: {} nombre: {} tipo: {}".format(self.codigo, self.nombre, self.tipo)

    # Creamos una clase meta para poder ponerle nombre singular y plurar al    producto
    # Tambien para cuando queramos oredenar nuestros productos definimos una forma
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']
