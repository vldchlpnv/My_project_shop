from django import template
from ..models import Category

register = template.Library()
@register.inclusion_tag('catalog/inclusion_tag_category.html')
def show_categories():

    all_categories = Category.objects.all()
    return {'all_categories':all_categories}

#@register.simple_tag
#def total_posts():

#    return Category.objects.all()