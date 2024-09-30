from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from productos.models import Producto, Categoria


def catalogo_de_productos(peticion_http: HttpRequest) -> HttpResponse:
    categoria_nombre = peticion_http.GET.get("categoria")
    termino_de_busqueda = peticion_http.GET.get("nombre")

    # Base query para productos
    productos = Producto.objects.all()

    # Filtrar por categoría si se proporciona
    if categoria_nombre:
        try:
            categoria = Categoria.objects.get(nombre=categoria_nombre)
            productos = productos.filter(categorias=categoria)
        except Categoria.DoesNotExist:
            categoria = None
    else:
        categoria = None

    # Filtrar por término de búsqueda si se proporciona
    if termino_de_busqueda:
        productos = productos.filter(nombre__icontains=termino_de_busqueda)

    # Contexto para la vista
    contexto_de_la_vista = {
        "items": productos,
        "categoria": categoria,
        "busqueda": termino_de_busqueda,
    }

    # Renderizar la plantilla
    return render(
        request=peticion_http,
        context=contexto_de_la_vista,
        template_name="productos/catalogo.html",
    )
