from django.urls import path

from orders.views import new_order, list_order
urlpatterns = [
    path('new_order/', new_order),
    path('list_order/', list_order)
]
