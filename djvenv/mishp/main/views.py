from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category, InstrumentsCatalog
from django.template.response import TemplateResponse
from django.http import Http404

def main_page(request):# представление списка товаров на странице а так же саппорт ссылки ( 100% рабочее)
    #support = ['Мои заказы', 'Доставка', 'Избранное', 'Отзывы', 'О нас', 'Контакты']
    category = Category.objects.all()

    #return render(request, 'main/main_page.html', {'support':support, 'category':category})
    return render(request, 'main/main_page.html', {'category':category})

def about(request):# представление для О нас --- Работает
    return render(request, 'main/about_us.html')

#def details(request):

#    guitar = Category.objects.get(id=1)
#    more_info = InstrumentsCatalog.objects.get(id=1)
#    return render(request, 'main/detail.html', {'guitar':guitar, 'more_info':more_info})

def details(request, id):
    try:
        guitar = Category.objects.get(id=id)

    except Category.DoesNotExist:
        raise Http404("No Post found.")

    return render(request,
                  'main/detail.html',
                  {'guitar':guitar})
