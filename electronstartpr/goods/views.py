from django.shortcuts import render

from .models import Catigories, Brands, Specifications, ProductSpecifications

def catalog(request):

    categories_in_catalog = Catigories.objects.all()
    brands = Brands.objects.all()
    specifications = Specifications.objects.all()
    product_specifications = ProductSpecifications.objects.all()
    context = {
        "title": "Каталог",
        "goods": [       
        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

         {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

         {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200},

        {'image': 'deps/img/avtomat.webp',
         'name': 'Автоматический выключатель 1P 16A',
         'description': 'Автоматический выключатель 1P 16A 6kA AC.',
         'article': 'DS202012',
         'brand': 'ABB',
         'price': 1200}, ],

         'categories_in_catalog': categories_in_catalog,
         'brands': brands,
         'specifications': specifications,
         'product_specifications': product_specifications,

    }

    return render(request, 'goods_templates/catalog.html', context)

def product(request):
    context = {
        "title": "Карточка"
    }
    return render(request, 'goods_templates/product.html', context)