from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Categories, Brands, Products, Quantity_of_poles, Rated_amperage, Rated_voltage, Amperage_type

def catalog(request):

    #Переменная все товары
    goods = Products.objects.all()

    #Переменные Тип устройства и бренды
    categories_in_catalog = Categories.objects.all()
    brands = Brands.objects.all()
    
    #Переменные характеристик
    product_quantity_of_poles = Quantity_of_poles.objects.all() #Кол-во полюсов
    product_rated_amperage = Rated_amperage.objects.all().order_by('value') #Ном.ток
    product_rated_voltage = Rated_voltage.objects.all() #Ном.напряжение
    product_amperage_type = Amperage_type.objects.all() #тип тока
       
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Каталог",
        "goods": current_page,

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