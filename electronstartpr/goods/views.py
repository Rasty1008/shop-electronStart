
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator

from django.db.models import IntegerField, F, Value
from django.db.models.functions import Cast, Replace

from .models import Categories, Brands, Products, Quantity_of_poles, Rated_amperage, Rated_voltage, Amperage_type
from .utils import q_search


def catalog(request, category_slug=None):

    #Переменные Тип устройства и бренды
    categories_in_catalog = Categories.objects.order_by('id')
    brands = Brands.objects.order_by('name')
    
    #Переменные характеристик
    product_quantity_of_poles = Quantity_of_poles.objects.annotate(
        q_of_pol_int = Cast(Replace(F('value'), Value('P'), Value('')), IntegerField())
        ).order_by('q_of_pol_int') #Кол-во полюсов

    product_rated_amperage = Rated_amperage.objects.annotate(
        voltage_int=Cast(Replace(F('value'), Value('A'), Value('')), IntegerField())
        ).order_by('voltage_int') #Номинальный ток

    product_rated_voltage = Rated_voltage.objects.annotate(
        voltage_int = Cast(Replace(F('value'), Value('V'), Value('')), IntegerField())
        ).order_by('voltage_int') #Ном.напряжение
    
    product_amperage_type = Amperage_type.objects.all() #тип тока
       
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all-categories':
        goods = Products.objects.all()

    elif query:
        goods = q_search(query)

    else:
        goods = Products.objects.filter(category_id__slug=category_slug)
        if not goods.exists():
            raise Http404()

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Каталог',
        'goods': current_page,
        'slug_category': category_slug,

        'categories_in_catalog': categories_in_catalog,
        'brands': brands,
        'product_quantity_of_poles': product_quantity_of_poles,
        'product_rated_amperage':  product_rated_amperage,
        'product_rated_voltage': product_rated_voltage,
        'product_amperage_type': product_amperage_type,

    }

    return render(request, 'goods_templates/catalog.html', context)



def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'title': 'Карточка товара',
        'product': product,
    }
    return render(request, 'goods_templates/product.html', context)