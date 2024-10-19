from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import settings

from .models import CartItems, Products
from .serializers import CartItemsSerializer, ProductsSerializer
from mishp.catalog.models import *

class CartView(APIView):
    def get(self, request, format=None):
        #read_catalog = InstrumentsCatalog.objects.all()
        get_cart = CartItems.objects.all() # тут должно быть пусто когда пустая корзина
        serializer = CartItemsSerializer(get_cart, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        add_in_cart =



