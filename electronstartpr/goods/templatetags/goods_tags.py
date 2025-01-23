from django import template

from goods.models import Catigories

register = template.Library()

#Все товары
@register.simple_tag()
def categories_tag():
    required_category = (2, 3, 5, 6, 7, 8, 12, 17, 18, 21, 22, 24)
    return Catigories.objects.filter(id__in=required_category)

