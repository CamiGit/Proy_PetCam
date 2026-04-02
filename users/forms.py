from django import forms

class UsersForms(forms.Form):
    name = forms.CharField(max_length=80)
    id_card = forms.FloatField()
    address = forms.CharField(max_length=100)
    phone = forms.IntegerField()