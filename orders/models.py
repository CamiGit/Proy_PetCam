from django.db import models

class Order (models.Model):
    number_order = models.IntegerField()
    name_client = models.CharField(max_length=80)
    time = models.DateField(auto_now= True)

