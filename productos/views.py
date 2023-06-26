from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .forms import ProductoForm
from .models import Producto
# Create your views here.

def index(request):
    productos=Producto.objects.all()
    return render(
        request,
        'index.html',
        context={'productos':productos}
    )

def detalle(request,producto_id):
    producto = Producto.objects.get(id=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto':producto}
    )

def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productos")
        
    form = ProductoForm()
    return render(
        request,
        "producto_form.html",
        {'form':form}
    )