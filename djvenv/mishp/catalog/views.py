from django.shortcuts import render
from django.http import Http404
from .models import *
from django.core.paginator import Paginator, EmptyPage


def details_of_category(request, slug):
    '''вернет типы типы инструментов бас,
     электро, акустика и тд'''

    category_of_instr = Category.objects.get(slug=slug) # этим запросом получим категорию инструменов ударные гитары клавиши или прочее
    type_of_instr_in_category = category_of_instr.showcaseofinstrumentst_set.filter(type_of_instruments_showcase_id=category_of_instr) # типы инструментов в категории бас, акустика, электро и тд

    return render(request, 'catalog/details_of_category.html', {'type_of_instr_in_category':type_of_instr_in_category})


def details(request, slug):
    '''описывает витрину с инструментами в каталоге'''
    #goods_in_category = InstrumentsCatalog.objects.filter(type_of_goods_id=id)
    goods_in_category_1 = ShowcaseOfInstrumentst.objects.get(slug=slug)
    goods_in_category = goods_in_category_1.instrumentscatalog_set.all()
    return render(request, 'catalog/detail.html', {'goods_in_category':goods_in_category})

#запрос:
#c = ShowcaseOfInstrumentst.objects.get(slug='amplifier-head')
#c_1 = c.instrumentscatalog_set.all()