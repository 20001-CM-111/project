from django.db import models
from django.contrib.auth.models import User
class Add_To_Cart(models.Model):
    ProductId=models.CharField(max_length=200)
    Price=models.CharField(max_length=20)
    Quantity=models.CharField(max_length=10)
    def __str__(self):
        return self.ProductId


# Create your models here.
