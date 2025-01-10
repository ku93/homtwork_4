from django.urls import path
from catalog.apps import CatalogConfig
from .views import home, contacts, product_detail, catalogs, product_list, category_deteil, category_list

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name='home'),
    path("contacts/", contacts, name='contacts'),
    path("catalogs/", catalogs, name='catalogs'),
    path('products/', product_list, name='product_list'),
    path('category/', category_list, name='category_list'),
    path("products/<int:pk>/", product_detail, name='product_detail'),
    path("category/<int:pk>/", category_deteil, name='category_deteil'),
    ]