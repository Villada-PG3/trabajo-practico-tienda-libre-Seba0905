""" from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ProductosTemplateView(TemplateView):
    template_name = "productos.html" """

from django.shortcuts import render
from .models import Producto

def productos(request):
    lista_productos = Producto.objects.all()

    contexto = {
        "productos": lista_productos
    }

    return render(request, "productos.html", contexto)