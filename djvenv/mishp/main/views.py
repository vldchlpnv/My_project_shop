from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category

def main_page(request):
    
    
    
    return render(request, 'main/main_page.html')


