from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    category = models.CharField(max_length=80)
    stock = models.BooleanField(default=True)