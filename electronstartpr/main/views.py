from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Catigories

def index(request):

    ids = (2, 3, 5, 6, 7, 8, 12, 17, 18, 21, 22, 24)
    categories = Catigories.objects.filter(id__in = ids)
    context = {
        'title': 'Электромаркет',
        'categories': categories,
    }

    return render(request, 'main_templates/index.html', context)

def contacts_page(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'main_templates/contacts.html', context)
