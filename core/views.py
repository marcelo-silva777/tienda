from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import  ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from .forms import RegistroForm

def list_products(request):
    # Obtener todos los productos
    products = Product.objects.all()

    # Puedes pasar la lista de productos a tu template HTML para mostrarla
    return render(request, 'products.html', {'products': products})

@method_decorator(login_required, name='dispatch')
class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy("list_products")

@method_decorator(login_required, name='dispatch')
class ProductList (ListView):
    model = Product
    template_name = 'list_product.html'

@method_decorator(login_required, name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit_product.html'
    success_url = reverse_lazy('list_product')

@method_decorator(login_required, name='dispatch')
class ProductDelete(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('list_product')




def home(request):
    return render(request, 'home.html')


def exit(request):
    logout(request)
    return redirect('home')


class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')