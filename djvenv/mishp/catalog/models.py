from django.db import models

class InstrumentsCatalog(models.Model):

    title = models.ForeignKey(Category, on_delete=models.CASCADE)    # фирма производитель
    slug = models.SlugFielg(unique=True)    # слаг
    model = models.CharField(max_length=100)    # модель инструмента
    availability = models.BooleanField()    # наличие
    quantity = models.IntegerField()    # количство
    price = models.IntegerField()    # цена


class Category(models.Model):

    type_of_instruments = models.CharField(max_length=100)    # тип инструмента

