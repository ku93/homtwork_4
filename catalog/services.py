from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получает список продуктов из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    cached_products = cache.get(key)
    if cached_products is not None:
        return cached_products
    cached_products = Product.objects.all()
    cache.set(key, cached_products, 60 * 5)
    return cached_products


def get_products_by_category(category):
    """Получает список продуктов по категории из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Product.objects.filter(category=category)
    key = f"products_by_category_{category.id}"
    cached_products = cache.get(key)
    if cached_products is not None:
        return cached_products
    cached_products = Product.objects.filter(category=category)
    cache.set(key, cached_products, 60 * 5)
    return cached_products
