from django import template
from urllib.parse import urlencode
from django.conf import settings
from django.core.cache import cache
from django.db.models import Case, When
from goods.models import Category, Brand

import json
import os
import logging

logger = logging.getLogger(__name__)
register = template.Library()

CATEGORY_JSON_PATH = getattr(settings, 'CATEGORY_JSON_PATH', 'electronstartpr/goods/templatetags/category_for_home_page.json')

'''
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
'''

@register.simple_tag()
def categories_tag():
    try:
        # попытка взять из кеша список PK
        cached_pks = cache.get('categories_tag')
        if cached_pks:
            preserve_order = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(cached_pks)])
            return list(Category.objects.filter(pk__in=cached_pks).order_by(preserve_order))

        # сформировать абсолютный путь к json
        json_path = CATEGORY_JSON_PATH
        if not os.path.isabs(json_path):
            json_path = os.path.join(settings.BASE_DIR, json_path)

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        list_categories = [n.strip() for n in data.get('required_category_name', []) if n and n.strip()]

        ordered = []
        found_pks = []
        for name in list_categories:
            cat = Category.objects.filter(name__iexact=name).first()
            if not cat:
                cat = Category.objects.filter(name__icontains=name).first()
            if cat and cat.pk not in found_pks:
                ordered.append(cat)
                found_pks.append(cat.pk)

        if not ordered:
            ordered = list(Category.objects.all()[:12])
            found_pks = [c.pk for c in ordered]

        cache.set('categories_tag', found_pks, 60 * 60)
        return ordered

    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.exception('Ошибка загрузки JSON: %s', e)
        return list(Category.objects.all()[:12])
    except Exception as e:
        logger.exception('Ошибка в categories_tag: %s', e)
        return list(Category.objects.all()[:12])
    
@register.simple_tag()
def brands_tag_cache():
    try:
        #Проверка кэша
        cached_pks = cache.get('brands_tag_cache')
        if cached_pks:
            preserve_order = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(cached_pks)])
            return list(Brand.objects.filter(pk__in=cached_pks).order_by(preserve_order))
        
        #Если в кэше нет, загружаем из базы
        brands = list(Brand.objects.all())
        found_pks = [b.pk for b in brands]

        #Кэшируем на 60 мин
        cache.set('brands_tag_cache', found_pks, 60 * 60)
        return brands
    
    except Exception as e:
        logger.exception('Ошибка в brands_tag_cache: %s', e)
        return []
        

    
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