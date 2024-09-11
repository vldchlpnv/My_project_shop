from django.urls import path, include
from . import views

app_name = 'catalog'

urlpatterns = [path('catalog/<int:id>/', views.details, name='details')]# Детали о категории