from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Cart_Items
from catalog.models import InstrumentsCatalog

@login_required
def cart_view(request):
    cart_items = Cart_Items.objects.filter(user=request.user)
    total_price = sum(item.goods_in_cart.price * item.quantity for item in cart_items)
    price = list(item.goods_in_cart.price * item.quantity for item in cart_items) # коллекция из цен в сумме за каждый товар
    #in_cart = list(item.goods_in_cart.slug for item in cart_items) # коллекция из товаров по слагам
    #quantity = list(item.quantity for item in cart_items) # количество каждого товара
    #price_in_cart = zip(in_cart, price, quantity)

    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})#, 'price_in_cart':price_in_cart})

#@login_required
#def cart_add(request, goods_in_cart_id):

    #product = get_object_or_404(InstrumentsCatalog, id=goods_in_cart_id)

    #cart_item, created = Cart_Items.objects.get_or_create(user=request.user, goods_in_cart=product)
    #if not created:
    #    cart_item.quantity += 1
    #    cart_item.save()
    #return redirect('cart_view')

@login_required
def cart_add(request, goods_in_cart_id):
    product = get_object_or_404(InstrumentsCatalog, id=goods_in_cart_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            cart_item, created = Cart_Items.objects.get_or_create(user=request.user, goods_in_cart=product)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            return redirect('cart_view')

        elif action == 'increase':
            cart_item, created = Cart_Items.objects.get_or_create(user=request.user, goods_in_cart=product)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            return redirect('cart_view')

        elif action == 'decrease':
            cart_item, created = Cart_Items.objects.get_or_create(user=request.user, goods_in_cart=product)
            if not created:
                cart_item.quantity -= 1
                cart_item.save()
            return redirect('cart_view')
    else:
        return render(request, 'cart/cart_detail.html')


