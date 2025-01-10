from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category

def _get_context(current_page):
    """Функция для создания общего контекста."""
    return {'current_page': current_page}

def home(request):
    products = Product.objects.all()
    context = _get_context('home')
    context.update({'products': products})
    return render(request, 'product_list.html', context)


def catalogs(request):
    categories = Category.objects.all()
    context = _get_context('catalogs')
    context.update({'categories': categories})
    return render(request, 'category_list.html', context)

def contacts(request):
    context = _get_context('contacts')
    return render(request, 'contacts.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_list.html', context)

def category_list(request):
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
    }
    return render(request, 'category_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def category_deteil(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {'category': category}
    return render(request, 'category_deteil.html', context)



