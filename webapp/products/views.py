from django.shortcuts import render, get_object_or_404, redirect
from ..models import Producto
from .forms import ProductoForm

def product_list(request):
    products = Producto.objects.all().order_by('-id')
    return render(request, 'products/index.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('products:list')
    else:
        form = ProductoForm()

    return render(request, 'products/create.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductoForm(instance=product)
    return render(request, 'products/edit.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:list')
    return render(request, 'products/delete.html', {'product': product})
