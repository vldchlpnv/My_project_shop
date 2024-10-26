from django.db import models
from django.contrib.auth.models import User
from catalog.models import InstrumentsCatalog

class Cart_Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods_in_cart = models.ForeignKey(InstrumentsCatalog, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity})"


