from django.urls import path
from catalog.apps import CatalogConfig
from .views import home, contacts

app_name = CatalogConfig.name
urlpatterns = [
    path("", home, name='home'),
    path("contacts/", contacts, name='contact'),
    path("categories/", contacts, name='categories'),
    path("categories/category_1/", contacts, name='category_1'),
    path("categories/category_2/", contacts, name='category_2'),
    path("categories/category_3/", contacts, name='category_3'),
    path("categories/category_4/", contacts, name='category_4')
]