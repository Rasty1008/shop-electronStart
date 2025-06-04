from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Brand


def index(request):
    brands = Brand.objects.all()
    context = {
        'title': 'Электромаркет',
        'brands': brands,
    }

    return render(request, 'main_templates/index.html', context)

def contacts_page(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'main_templates/contacts.html', context)
