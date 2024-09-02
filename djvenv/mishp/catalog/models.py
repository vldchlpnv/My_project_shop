from django.db import models

class Instruments(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugFielg()
    model = models.CharField(max_length=100)
    availability = models.BooleanField()
    quantity = models.IntegerField()
    price = models.IntegerField()

    

# Create your models here.
