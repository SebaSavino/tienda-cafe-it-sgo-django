from django.contrib import admin

from productos.models import Producto, Categoria

admin.site.register([Producto, Categoria])
