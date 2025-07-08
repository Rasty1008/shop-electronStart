from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .models import Product

def q_search(query):
    """"Функция поиска товаров"""
    
    #vector = SearchVector('name', 'description', 'article')
    #query = SearchQuery(query)

    #return Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')
    
    #return Product.objects.filter(article__iexact=query)
    
    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(name__icontains=token)
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(article__icontains=token)

    return Product.objects.filter(q_objects) 

def filter_goods(request, queryset):
    """ Фильтрует товары по Get запросам """

    # Получаем параметры фильтрации из GET-запроса
    query = request.GET.get('q', None) # Поиск по названию
    selected_category = request.GET.get('category')  # Тип устройства
    selected_brands = request.GET.getlist('brand')  # Бренды
    selected_poles = request.GET.getlist('poles')  # Количество полюсов
    selected_amperages = request.GET.getlist('amperage')  # Номинальный ток
    selected_voltages = request.GET.getlist('voltage')  # Номинальное напряжение
    selected_amperage_types = request.GET.getlist('amperage_type')  # Тип тока


    if query:
        queryset = q_search(query)
    if selected_category:
        queryset = queryset.filter(category__slug=selected_category)
    if selected_brands:
        queryset = queryset.filter(brand__slug__in=selected_brands)
    if selected_poles:
        queryset = queryset.filter(quantity_of_poles__value__in=selected_poles)
    if selected_amperages:
        queryset = queryset.filter(rated_amperage__value__in=selected_amperages)
    if selected_voltages:
        queryset = queryset.filter(rated_voltage__value__in=selected_voltages)
    if selected_amperage_types:
        queryset = queryset.filter(amperage_type__value__in=selected_amperage_types)

    order_by = request.GET.get('order_by', 'default')
    if order_by and order_by != 'default':
        queryset = queryset.order_by(order_by)

    selected_filters = {
        'selected_category': selected_category,
        'selected_brands': selected_brands,
        'selected_poles': selected_poles,
        'selected_amperages': selected_amperages,
        'selected_voltages': selected_voltages,
        'selected_amperage_types': selected_amperage_types,
        'order_by': order_by,
    }
        
    return queryset, selected_filters


