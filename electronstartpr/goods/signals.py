from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from goods.models import Category, Brand, Product

@receiver([post_save, post_delete], sender=Product)
def invalidate_product_cache(sender, instance, **kwargs):
    """
    Удаляет кэш для конкретного продукта при его изменении
    """
    key = make_template_fragment_key('product_card', [instance.id])
    cache.delete(key)
    cache.delete('categories_tag')
    cache.delete('brands_tag_cache')

@receiver([post_save, post_delete], sender=Category)
@receiver([post_save, post_delete], sender=Brand)
def invalidate_caches(sender, instance, **kwargs):
    """
    Удаляет ключи кэша при изменении моделей
    """
    cache.delete('categories_tag')
    cache.delete('brands_tag_cache')