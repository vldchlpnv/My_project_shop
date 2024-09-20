from django.shortcuts import render
from django.http import Http404
from .models import Category, InstrumentsCatalog
from django.core.paginator import Paginator, EmptyPage


def details_of_category(request, id):

    category_of_instr = Category.objects.get(id=id) # этим запросом получим категорию инструменов ударные гитары клавиши или прочее
    type_of_instr_in_category = category_of_instr.showcaseofinstrumentst_set.filter(type_of_instruments_showcase_id=category_of_instr) # типы инструментов в категории бас, акустика, электро и тд

    return render(request, 'catalog/details_of_category.html', {'type_of_instr_in_category':type_of_instr_in_category})


def details(request, id):

    req_2 = InstrumentsCatalog.objects.filter(type_of_goods_id=id)
    return render(request, 'catalog/detail.html', {'req_2':req_2})

