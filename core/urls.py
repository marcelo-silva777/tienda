from django.urls import path
from . import views
from .views import home, exit
from .views import RegistroView

urlpatterns = [
    # Otras URLs de tu aplicación

    # URL para listar productos por categoría, con un parámetro de ID
    path('', home, name='home'),
    path('list_products', views.list_products, name='list_products'),
    path('add_product', views.ProductCreate.as_view() , name='add_product'),
    path('list_product', views.ProductList.as_view() , name='list_product'),
    path('delete_product/<int:pk>', views.ProductDelete.as_view() , name="delete_product"),
    path('edit_product/<int:pk>', views.ProductUpdate.as_view() , name="edit_product"),
    path('logout/', exit, name='exit'),
    path('registro/', RegistroView.as_view(), name='registro'),
    
]

