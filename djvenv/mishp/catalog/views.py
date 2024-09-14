from django.shortcuts import render
from django.http import Http404
from .models import Category, InstrumentsCatalog
from django.core.paginator import Paginator, EmptyPage



def details(request, id):
    '''ф.п. перекидывающая нас
    на шаблон описывающий внутрянку каждой категории'''

    inst_cat = InstrumentsCatalog.objects.filter(type_of_instruments_id=id).values()  # получим queryset из словарей
    # со всеми данными в бд по выбранным объектам.
    # ------------------------------------------------------------------
    paginator = Paginator(inst_cat, 5)  # создаем экземпляр класса Paginator для постраничной разбивки
    page_number = request.GET.get('page', 1)
    instruments_pages = paginator.page(page_number)
    # ------------------------------------------------------------------
    instruments_catalog = InstrumentsCatalog.objects.get(id=id)  # извлекаем все оъекты из таблицы InstrumentsCatalog

    try:
        head_of_page = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404('Post not found')

    return render(request,
                  'catalog/detail.html',
                  {'head_of_page':head_of_page, 'instruments_catalog':instruments_catalog, 'instruments_pages':instruments_pages})
