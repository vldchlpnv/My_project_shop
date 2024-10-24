from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import settings

from .models import CartItems, Products
from .serializers import CartItemsSerializer, InstrumentsCatalogSerializer
from catalog.models import * # тут тоже убрал mishp
from rest_framework import status

class CartView(APIView):
    def get(self, request, format=None):    #   +
        get_cart = CartItems.objects.filter(user=request.user)
        serializer = CartItemsSerializer(get_cart, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartItemsSerializer(data=request.data)
        if serializer.is_valid():
            # Получаем ID инструмента напрямую
            instruments_catalog_id = serializer.validated_data[
                'instruments_catalog'].id  # Проверяем, существует ли товар
            product = InstrumentsCatalog.objects.filter(id=instruments_catalog_id).first()
            if product is None:
                return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

                # Проверяем, есть ли уже этот товар в корзине
                cart_item, created = CartItems.objects.get_or_create(
                user = request.user,
                product = product,
                defaults = {'quantity': 0}
            )

            # Увеличиваем количество, если товар уже в корзине
            cart_item.quantity += serializer.validated_data['quantity']
            cart_item.save()

            return Response(CartItemsSerializer(cart_item).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





