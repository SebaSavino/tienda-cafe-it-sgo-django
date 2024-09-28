from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from productos.models import Producto


def catalogo_de_productos(peticion_http: HttpRequest) -> HttpResponse:
    # Busco los productos en mi base de datos
    productos = Producto.objects.all()

    # Los agrego al contexto para poder mostrarlos en una plantilla (template, archivo html)
    contexto_de_la_vista = {"items": productos}

    # Renderizo la plantilla con toda la información que junté
    return render(
        request=peticion_http,
        context=contexto_de_la_vista,
        template_name="productos/catalogo.html",
    )
