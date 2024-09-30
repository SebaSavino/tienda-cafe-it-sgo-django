from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)

    class Meta:
        db_table = "categorias"
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)
    nombre = models.CharField(max_length=250, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    categorias = models.ManyToManyField(Categoria)

    class Meta:
        # Nombre de la tabla en la base de datos SQL
        db_table = "productos"

        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
