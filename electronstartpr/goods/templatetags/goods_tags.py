from django import template

from goods.models import Categories

register = template.Library()

#Все товары
@register.simple_tag()
def categories_tag():
    required_category = (1, 2, 4, 5, 6, 7, 11, 16, 17, 20, 21, 23)

    return Categories.objects.filter(id__in=required_category)

