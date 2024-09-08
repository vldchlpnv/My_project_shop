from django.urls import path
from . import views

app_name = 'main' # именное пространство

urlpatterns = [path('', views.main_page, name='main_page'),
               path('about/', views.about, name='about'),# О нас
               path('<int:id>/', views.details, name='details')]# Детали о категории

#path('details/', views.details, name='details')