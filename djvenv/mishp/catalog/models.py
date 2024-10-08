from django.db import models


class Category(models.Model):

    type_of_instruments = models.CharField(max_length=100)    # тип инструмента
    slug = models.SlugField(null=True)

    class Meta:

        ordering = ['slug']

    def __str__(self):
        return self.type_of_instruments

class ShowcaseOfInstrumentst(models.Model): # Модель с типами товаров электро, бас, акустика, пластик, комбо, голова, кабинет, и т.д.

    goods = models.CharField(max_length=100)
    slug = models.SlugField()
    type_of_instruments_showcase = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.goods


class InstrumentsCatalog(models.Model):

    title = models.CharField(max_length=100)    # фирма производитель
    slug = models.SlugField(unique=True)    # слаг
    model = models.CharField(max_length=100)    # модель инструмента
    availability = models.BooleanField()    # наличие
    quantity = models.IntegerField()    # количство
    price = models.IntegerField()    # цена
    type_of_instruments = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)  # тип инструмента
    type_of_goods = models.ForeignKey(ShowcaseOfInstrumentst, on_delete=models.CASCADE, null=True)

    class Meta:

        ordering = ['slug']

    def __str__(self):
        return self.title

# Добавить индексацию




