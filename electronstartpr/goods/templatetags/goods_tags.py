from django import template
from urllib.parse import urlencode
from django.conf import settings
from django.core.cache import cache
from django.db.models import Case, When
from goods.models import Category

import json

register = template.Library()

CATEGORY_JSON_PATH = getattr(settings, 'CATEGORY_JSON_PATH', 'electronstartpr/goods/templatetags/category_for_home_page.json')


@register.simple_tag()
def categories_tag():
    try:
        # Проверка кэша
        categories = cache.get('categories_tag')
        if not categories:
            with open(CATEGORY_JSON_PATH, 'r') as f:
                list_of_categories_in_the_file = json.load(f)
                list_categories = list_of_categories_in_the_file['required_category_name']

            # Сохранение порядка категорий
            preserve_order = Case(*[When(name=name, then=pos) for pos, name in enumerate(list_categories)])
            categories = Category.objects.filter(name__in=list_categories).order_by(preserve_order)

            # Кеширование результата
            cache.set('categories_tag', categories, 60 * 60) # Кэшируем на 60 мин
        return categories
    except(FileNotFoundError, json.JSONDecodeError) as e:
        return Category.objects.none() # В случае ошибки возврат пустого QuerySet
    
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.copy()
    for key, value in kwargs.items():
        # Если значение — список, берём только первый элемент
        if isinstance(value, (list, tuple)):
            query[key] = str(value[0])
            #query.setlist(key, [str(v) for v in value])
        else:
            query[key] = str(value)
    return query.urlencode()



@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()