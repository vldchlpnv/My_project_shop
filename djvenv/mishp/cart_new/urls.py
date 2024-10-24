from . import views
from django.urls import path

from django.urls import path
from . import views

#app_name = 'cart_new'

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<int:goods_in_cart_id>/', views.cart_add, name='cart_add'),

]

#path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),