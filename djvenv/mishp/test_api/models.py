from django.db import models
from django.contrib.auth.models import User
from catalog.models import InstrumentsCatalog

class Products(models.Model):   # не используется
    name = models.CharField(max_length=150)
    price = models.IntegerField()


    def __str__(self):
        return self.name

class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(InstrumentsCatalog, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.quantity}'


