from django.urls import path
from .views import carrito, home, galeria, inicio, listado_libro, nuevo_libro, modificar_libro, eliminar_libro, registro_usuario,inicio

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('listado-libro/', listado_libro, name="listado_libros"),
    path('nuevo-libro/', nuevo_libro, name="nuevo_libro"),
    path('modificar-libro/<id>/', modificar_libro, name="modificar_libro"),
    path('eliminar-libro/<id>/', eliminar_libro, name="eliminar_libro"),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('inicio/', inicio, name="ini" ),
    path('carrito/', carrito,name="carrito")
]
