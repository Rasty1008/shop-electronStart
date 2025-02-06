from django import template
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()

#Выбранные товары на главной странице
@register.simple_tag()
def categories_tag():
    required_category = (1, 2, 4, 5, 6, 7, 11, 16, 17, 20, 21, 23)

    return Categories.objects.filter(id__in=required_category)

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

