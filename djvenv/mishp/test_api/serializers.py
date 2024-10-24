from rest_framework import serializers
from .models import CartItems
from catalog.models import InstrumentsCatalog # туту было исправление

class InstrumentsCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'slug', 'price', 'availability')
        model = InstrumentsCatalog


class CartItemsSerializer(serializers.ModelSerializer):
    instruments_catalog = serializers.PrimaryKeyRelatedField(queryset=InstrumentsCatalog.objects.all())

    class Meta:
        fields = ('id', 'quantity', 'instruments_catalog')
        model = CartItems
        