from django.urls import path
from catalog.apps import CatalogConfig
from .views import home, catalogs, contacts, product_deteil, category_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name='home'),
    path("catalogs", catalogs, name='catalogs'),
    path('contacts', contacts, name='contacts'),
    path('products/<int:pk>', product_deteil, name='product_deteil'),
    path('categorys/<int:pk>', category_detail, name='category_detail'),
    ]