from django.urls import path
from .views import *


urlpatterns = [path('singin/', ViewForRegistration.as_view(), name='ViewForRegistration')]