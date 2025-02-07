from django import template
from django.utils.http import urlencode

from goods.models import Categories

import json


register = template.Library()

#Выбранные товары на главной странице
@register.simple_tag()
def categories_tag():
    with open('electronstartpr/goods/templatetags/category_for_home_page.json', 'r') as f:
        list_of_categories_in_the_file = json.load(f)
        list_categories = list_of_categories_in_the_file['required_category_name']

    return Categories.objects.filter(name__in=list_categories)

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

