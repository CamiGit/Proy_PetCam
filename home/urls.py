from django.urls import path

from home.views import new_category, list_category

urlpatterns = [
    path('new_category/', new_category),
    path('list_category/', list_category)

]
