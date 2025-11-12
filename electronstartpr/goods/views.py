from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Category, Brand, Product, QuantityOfPoles, RatedAmperage, RatedVoltage, AmperageType
from .utils import filter_goods


class CatalogListView(ListView):
    model = Product
    template_name = 'goods_templates/catalog.html'
    context_object_name = 'goods'
    paginate_by = 24
    allow_empty = True

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset, self.selected_filters = filter_goods(self.request, queryset)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Каталог',
            'categories_in_catalog': Category.objects.all(),
            'brands': Brand.objects.all(),
            'product_quantity_of_poles': QuantityOfPoles.objects.all(),
            'product_rated_amperage': RatedAmperage.objects.all(),
            'product_rated_voltage': RatedVoltage.objects.all(),
            'product_amperage_type': AmperageType.objects.all(),
            **getattr(self, 'selected_filters', {}),
        })
        return context

class ProductDetailView(DetailView):
    template_name = 'goods_templates/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_object(self, queryset=None):
        product = Product.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

#def catalog(request):

    # Переменные Тип устройства и бренды
    #categories_in_catalog = Category.objects.all()
    #brands = Brand.objects.all()
    
    # Переменные характеристик
    #product_quantity_of_poles = QuantityOfPoles.objects.all()
    #product_rated_amperage = RatedAmperage.objects.all()
    #product_rated_voltage = RatedVoltage.objects.all()
    #product_amperage_type = AmperageType.objects.all()

    #goods = Product.objects.all()
    #goods, selected_filters = filter_goods(request, goods)
       
    # Пагинация
    #paginator = Paginator(goods, 3)
    #page = request.GET.get('page')
    #current_page = paginator.get_page(page)   

    #context = {
    #    'title': 'Каталог',
    #    'goods': current_page,
    #    'categories_in_catalog': categories_in_catalog,
    #    'brands': brands,
    #    'product_quantity_of_poles': product_quantity_of_poles,
    #    'product_rated_amperage': product_rated_amperage,
    #    'product_rated_voltage': product_rated_voltage,
    #    'product_amperage_type': product_amperage_type,
    #    **selected_filters,
    #}

    #return render(request, 'goods_templates/catalog.html', context)


#def product(request, product_slug):
#    product = get_object_or_404(Product, slug=product_slug)
#    context = {
#       'title': 'Карточка товара',
#        'product': product,
#    }
#    return render(request, 'goods_templates/product.html', context)