from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductListView, ProductDetailView, CategoryListView, CategoryProductsView, Contacts, \
    CategoryCreateView, ProductCreateView, CategoryUpdateView, ProductUpdateView, CategoryDeleteView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='home'),
    path("catalogs", CategoryListView.as_view(), name='catalogs'),
    path('/contacts', Contacts.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/<int:pk>/', CategoryProductsView.as_view(), name='category_products'),
    path('categories/create', CategoryCreateView.as_view(), name='categories_create'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('categories/<int:pk>/update', CategoryUpdateView.as_view(), name='category_update'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('categories/<int:pk>/delete', CategoryDeleteView.as_view(), name='category_delete'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    ]