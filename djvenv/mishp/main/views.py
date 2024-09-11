from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category, InstrumentsCatalog


def main_page(request):# представление списка товаров на странице а так же саппорт ссылки ( 100% рабочее)
    #support = ['Мои заказы', 'Доставка', 'Избранное', 'Отзывы', 'О нас', 'Контакты']
    category = Category.objects.all()

    #return render(request, 'main/main_page.html', {'support':support, 'category':category})
    return render(request, 'main/main_page.html', {'category':category})

def about(request):# представление для О нас --- Работает
    return render(request, 'main/about_us.html')



