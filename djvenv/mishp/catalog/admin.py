from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['type_of_instruments', 'slug']
    prepopulated_fields = {'slug':('type_of_instruments',)}

@admin.register(InstrumentsCatalog)
class InstrumentsCatalogAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug', 'model', 'availability', 'quantity', 'price', 'type_of_instruments', 'type_of_goods']      # поля отображения
    list_filter = ['type_of_instruments', 'availability', 'title', 'type_of_goods']     # фильтрация по полям кторые включены в список
    search_fields = ['title', 'model']      # поиск по полям в целом удобно
    prepopulated_fields = {'slug': ('model',)}      #будем предзаполнять слаг из поля модель инструмента

@admin.register(ShowcaseOfInstrumentst)
class ShowcaseOfInstrumentstAdmin(admin.ModelAdmin):

    list_display = ['goods', 'slug', 'type_of_instruments_showcase']
    prepopulated_fields = {'slug':('goods',)}