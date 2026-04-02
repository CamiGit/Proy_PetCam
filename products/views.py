from django.shortcuts import render

from products.models import Product
from products.forms import ProductsForms

def new_product(request):
        if request.method == 'GET':
            context = {
                'form' : ProductsForms
            }
            return render(request, 'Products/Product_new.html', context=context)
        
        elif request.method == 'POST':
            form = ProductsForms(request.POST)
            if form.is_valid():
                Product.objects.create(
                    name = form.cleaned_data['name'],
                    price = form.cleaned_data['price'],
                    category = form.cleaned_data['category'],
                    stock = form.cleaned_data['stock']
                )
                context = {
                    'message' : 'Producto Creado'
                }
                return render(request, 'Products/Product_new.html', context=context)
            else:
                context = {
                    'form_errors' : form.errors,
                    'form' : ProductsForms
                }
                return render(request, 'Products/Product_new.html', context=context)

def list_product(request):
    Product_all = Product.objects.all()
    context = {
        'products' : Product_all
    }
    return render(request, 'Products/Product_list.html', context=context)

