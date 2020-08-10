from django.urls import path
from .views import crear_producto, ListarProductoView, editar_producto, eliminar_producto
# Creación de los paths
urlpatterns = [
    path('crear_producto', crear_producto, name='crear_producto'),
    path('listar_producto', ListarProductoView.as_view(), name='listar_producto'),
    path('editar_producto/<int:codigo>',
         editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:codigo>',
         eliminar_producto, name='eliminar_producto'),
]
