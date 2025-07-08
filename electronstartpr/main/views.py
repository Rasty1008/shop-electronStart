from django.views.generic import TemplateView
from goods.models import Brand
from django.conf import settings

class IndexView(TemplateView):
    template_name = 'main_templates/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Электромаркет'
        context['brands'] = Brand.objects.all()
        context['google_maps_iframe'] = settings.GOOGLE_MAPS_IFRAME
        return context
    
class ContactsView(TemplateView):
    template_name = 'main_templates/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['google_maps_iframe'] = settings.GOOGLE_MAPS_IFRAME
        return context

