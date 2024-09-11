from django.shortcuts import render
from django.http import Http404
from .models import Category, InstrumentsCatalog


def details(request, id):
    '''ф.п. перекидывающая нас
    на шаблон описывающий внутрянку каждой категории'''

    instruments_catalog = InstrumentsCatalog.objects.get(id=id)  # извлекаем все оъекты из таблицы InstrumentsCatalog
    instruments_catalog_all = InstrumentsCatalog.objects.filter(type_of_instruments_id=id)

    inst_cat = InstrumentsCatalog.objects.filter(type_of_instruments_id=id).values() # получим queryset из словарей
    # со всеми данными в бд по выбранным объектам

    try:
        guitar = Category.objects.get(id=id)
        instruments_catalog = InstrumentsCatalog.objects.get(id=id)  # извлекаем все оъекты из таблицы InstrumentsCatalog(!!!проверить на правильность!!!)
    except Category.DoesNotExist:
        raise Http404('Post not found')

    return render(request,
                  'catalog/detail.html',
                  {'guitar':guitar, 'instruments_catalog':instruments_catalog, 'instruments_catalog_all':instruments_catalog_all, 'inst_cat':inst_cat})

#'instruments_catalog_all':instruments_catalog_all