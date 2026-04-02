from django import forms

class OrdersForms(forms.Form):
    number_order = forms.IntegerField()
    name_client = forms.CharField()
    time = forms.DateTimeField()