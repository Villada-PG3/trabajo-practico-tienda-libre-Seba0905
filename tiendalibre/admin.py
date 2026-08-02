from django.contrib import admin
from django.utils.html import format_html

from .models import Producto, Categoria


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("vista_previa_imagen",)

    def vista_previa_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px;">',
                obj.imagen.url
            )
        return "No hay imagen"

    vista_previa_imagen.short_description = "Vista previa"


admin.site.register(Categoria)