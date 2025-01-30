from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Catigories, Brands, Specifications, ProductSpecifications, Products

def catalog(request):

    page = request.GET.get('page', 1)

    goods = Products.objects.all()

    #Переменные Тип устройства и бренды
    categories_in_catalog = Catigories.objects.all()
    brands = Brands.objects.all()
    
    #Переменные характеристик   
    quantity_of_poles = Specifications.objects.get(id=1) #Кол-во полюсов
    rated_amperage = Specifications.objects.get(id=2) #Ном.ток
    rated_voltage = Specifications.objects.get(id=3) #Ном.напряжение
    amperage_type = Specifications.objects.get(id=4) #тип тока

    #Переменные характеристик продукта
    product_quantity_of_poles = ProductSpecifications.objects.filter(value__endswith='P').distinct() #Кол-во полюсов
    product_rated_amperage = ProductSpecifications.objects.filter(value__endswith='A').values_list('value', flat=True).distinct() #Номинальный ток
    product_rated_voltage = ProductSpecifications.objects.filter(value__endswith='V').values_list('value', flat=True).distinct() #Номинальное напряжение
    product_amperage_type = ProductSpecifications.objects.filter(value__in=['AC', 'DC', 'AC-DC']).distinct() #Тип тока

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Каталог",
        "goods": current_page,

         'categories_in_catalog': categories_in_catalog,
         'brands': brands,

         'quantity_of_poles': quantity_of_poles,
         'rated_amperage': rated_amperage,
         'rated_voltage': rated_voltage,
         'amperage_type': amperage_type,

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