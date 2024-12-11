from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Электромаркет',
    }

    return render(request, 'main_templates/index.html', context)

def contacts_page(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'main_templates/contacts.html', context)
