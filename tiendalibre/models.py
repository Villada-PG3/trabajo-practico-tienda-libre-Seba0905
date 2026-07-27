from pyclbr import Class

from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"
        Ordering = ["nombre"]


class Producto(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos", null=True, blank=True)
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)
    activa = models.BooleanField(default=True)
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - {self.precio} - {self.stock}"
