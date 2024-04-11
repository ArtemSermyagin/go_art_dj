from django.core.cache import cache

from catalog.models import Category
from config import settings


def get_categories_from_cache():
    queryset = Category.objects.all()
    if not settings.CACHE_ENABLED:
        return queryset
    key = 'categories'
    cache_data = cache.get(key)
    if cache_data is None:
        cache_data = queryset
        cache.set(key, cache_data)
    return cache_data
