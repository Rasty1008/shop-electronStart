from django.shortcuts import render

def catalog(request):
    context = {
        "title": "Каталог"
    }

    return render(request, 'goods_templates/catalog.html', context)

def product(request):
    context = {
        "title": "Карточка"
    }
    return render(request, 'goods_templates/product.html', context)