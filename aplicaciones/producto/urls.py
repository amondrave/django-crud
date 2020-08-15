from django.urls import path
from .views import CrearProductoView, ListarProductoView, EditarProductoView, EliminarProductoView
# Creación de los paths
urlpatterns = [
    path('crear_producto', CrearProductoView.as_view(), name='crear_producto'),
    path('listar_producto', ListarProductoView.as_view(), name='listar_producto'),
    path('editar_producto/<int:pk>',
         EditarProductoView.as_view(), name='editar_producto'),
    path('eliminar_producto/<int:pk>',
         EliminarProductoView.as_view(), name='eliminar_producto'),
]
