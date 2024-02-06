from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ProductForm

def list_products(request):
    # Obtener todos los productos
    products = Product.objects.all()

    # Puedes pasar la lista de productos a tu template HTML para mostrarla
    return render(request, 'products.html', {'products': products})


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy("list_products")

class ProductList (ListView):
    model = Product
    template_name = 'list_product.html'

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit_product.html'
    success_url = reverse_lazy('list_product')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('list_product')
