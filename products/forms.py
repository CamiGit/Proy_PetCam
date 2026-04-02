from django import forms

class ProductsForms(forms.Form):
    name = forms.CharField(max_length=80)
    price = forms.IntegerField()
    category = forms.CharField(max_length=80)
    stock = forms.BooleanField(required=False)