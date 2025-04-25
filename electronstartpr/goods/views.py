
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Category, Brand, Product, QuantityOfPoles, RatedAmperage, RatedVoltage, AmperageType
from .utils import q_search


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




def catalog(request):

    # Переменные Тип устройства и бренды
    categories_in_catalog = Category.objects.all()
    brands = Brand.objects.all()
    
    # Переменные характеристик
    product_quantity_of_poles = QuantityOfPoles.objects.all()
    product_rated_amperage = RatedAmperage.objects.all()
    product_rated_voltage = RatedVoltage.objects.all()
    product_amperage_type = AmperageType.objects.all()

    goods = Product.objects.all()
    goods, selected_filters = filter_goods(request, goods)
       
    # Пагинация
    paginator = Paginator(goods, 3)
    page = request.GET.get('page')
    current_page = paginator.get_page(page)   

    context = {
        'title': 'Каталог',
        'goods': current_page,
        'categories_in_catalog': categories_in_catalog,
        'brands': brands,
        'product_quantity_of_poles': product_quantity_of_poles,
        'product_rated_amperage': product_rated_amperage,
        'product_rated_voltage': product_rated_voltage,
        'product_amperage_type': product_amperage_type,
        **selected_filters,
    }

    return render(request, 'goods_templates/catalog.html', context)


def product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'title': 'Карточка товара',
        'product': product,
    }
    return render(request, 'goods_templates/product.html', context)