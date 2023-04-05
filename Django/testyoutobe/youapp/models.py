from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.second_name} {self.name}"


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)