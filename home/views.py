from django.shortcuts import render
from django.http import HttpResponse

from home.models import Category
from home.forms import CategoryForms

def new_category(request):
    
    if request.method == 'GET':
        context = {
            'form' : CategoryForms
        }
        return render(request, 'Categories/Category_new.html', context=context)

    elif request.method == 'POST':
        form = CategoryForms(request.POST)
        if form.is_valid():
            Category.objects.create(name = form.cleaned_data['name'])
            context = {
                'message' : 'Categoria Creada'
            }
            return render(request, 'Categories/Category_new.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form' : CategoryForms
            }
            return render(request, 'Categories/Category_new.html', context=context)
    

def list_category(request):
    if 'search' in request.GET:
        search = request.GET['search']
        Category_all = Category.objects.filter(name = search)
    else:
        Category_all =  Category.objects.all()
    context = {
        'category': Category_all
    }
    return render(request, 'Categories/Category_list.html', context=context)
