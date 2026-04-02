from django.shortcuts import render

from users.models import User
from users.forms import UsersForms


def new_user(request):
    if request.method == 'GET':
        context = {
            'form' : UsersForms
        }
        return render(request, 'Users/User_new.html', context=context)

    elif request.method == 'POST':
        form = UsersForms(request.POST)
        if  form.is_valid():
            User.objects.create(
                name = form.cleaned_data['name'],
                id_card = form.cleaned_data['id_card'],
                address = form.cleaned_data['address'],
                phone = form.cleaned_data['phone']
            )
            context = {
                'message' : 'Usuario Creado'
            }
            return render(request, 'Users/User_new.html', context=context)
        else:
            context = {
                'form_errors' : form.errors,
                'form' : UsersForms
            }
            return render(request, 'Users/User_new.html', context=context)


def list_user(request):
    User_all = User.objects.all()
    context = {
        'user' : User_all
    }
    return render(request, 'Users/user_list.html', context=context)