from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products, 'current_page': 'home'})

def catalogs(request):
    categorys = Category.objects.all()
    return render(request, 'catalogs.html', {'categorys': categorys, 'current_page': 'catalogs'})

def contacts(request):
    return render(request, 'contacts.html', {'current_page': 'contacts'})

def product_deteil(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_deteil.html', {"product" : product, 'current_page': 'home'})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category_id=pk)
    return render(request, 'category_deteil.html', {
        'products': products,
        'current_page': 'catalogs',
        'category': category
    })



