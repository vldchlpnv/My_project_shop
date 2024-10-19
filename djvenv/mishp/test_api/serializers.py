from rest_framework import serializers
from .models import Products, CartItems

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Products

class CartItemsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()  # вот это будет вложенный сериализатор, что-то вроде такой записи получится
    # {"id": 1,"product": {"id": 2, "name": "Продукт 1","price": 100}, "quantity": 3}
    class Meta:
        fields = ('id', 'quantity')
        model = CartItems
        