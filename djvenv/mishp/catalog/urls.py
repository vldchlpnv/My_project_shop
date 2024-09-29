from django.urls import path, include
from . import views

app_name = 'catalog'

urlpatterns = [path('catalog/details/<slug:slug>/', views.details, name='details'),
               path('catalog/<slug:slug>/', views.details_of_category, name='details_of_category'),
               ]

