from django.db import models
from django.contrib.auth.models import User
#from mishp.catalog.models import InstrumentsCatalog

class Products(models.Model):
    name = models.CharField(max_length=150)     # сюда подавать слаг из модели инструментов
    price = models.IntegerField()


    def __str__(self):
        return self.name

class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'


