from django.urls import path, include
from . import views

app_name = 'catalog'

urlpatterns = [path('catalog/details/<int:id>/', views.details, name='details'),
               path('catalog/<int:id>/', views.details_of_category, name='details_of_category')]# Детали о категории

