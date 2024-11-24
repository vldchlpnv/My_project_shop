from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'main' # именное пространство

urlpatterns = [path('', views.main_page, name='main_page'),
               path('about/',TemplateView.as_view(template_name='main/about_us.html'), name='about'),
               path('delivery_and_payment/', TemplateView.as_view(template_name='main/delivery.html'), name='delivery_and_payment')
               ]
