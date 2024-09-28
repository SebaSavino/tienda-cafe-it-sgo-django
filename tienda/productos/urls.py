from django.urls import path

from productos.views import catalogo_de_productos

app_name = "productos"

urlpatterns = [path("", catalogo_de_productos, name="catalogo")]
