from django.shortcuts import render
from django.http import HttpResponse

from orders.models import Order
from orders.forms import OrdersForms

def new_order(request):

    if request.method == 'GET':
        context = {
            'form' : OrdersForms
        }
        return render(request, 'Orders/Order_new.html', context=context)

    elif request.method == 'POST':
        form =  OrdersForms(request.POST)
        if form.is_valid():
            Order.objects.create(
                number_order = form.cleaned_data['number_order'],
                name_client = form.cleaned_data['name_client'],
                time = form.cleaned_data['time']
            )
            context = {
                'message' : 'Orden Creada'
            }
            return render(request, 'Orders/Order_new.html', context=context)
        else:
            context = {
                'form_errors' : form.errors,
                'form': OrdersForms
            }
            return render(request, 'Orders/Order_new.html', context=context)

def list_order(request):
    Order_all = Order.objects.all()
    context = {
        'order' : Order_all
    }
    return render(request, 'Orders/Order_list.html', context=context)

