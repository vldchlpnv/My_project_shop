from django.contrib import admin
from .models import *
from catalog.models import InstrumentsCatalog


@admin.register(Cart_Items)
class Cart_Items(admin.ModelAdmin):

    list_display = ['user', 'goods_in_cart', 'quantity', 'name_of_goods', 'price']
    search_fields = ['user']
    def name_of_goods(self, obj): # имя метода это имя столбца в таблице
        return obj.goods_in_cart.slug # obj это есть обьект Cart_Items

    def price(self, obj):
        return obj.goods_in_cart.price * obj.quantity



