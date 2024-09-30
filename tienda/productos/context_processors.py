from productos.models import Categoria


def categorias(_):
    return {"categorias": Categoria.objects.all().values("nombre")}
