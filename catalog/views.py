from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'home'
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'catalogs'
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'catalogs'
        return context


class CategoryProductsView(ListView):
    model = Product
    template_name = 'catalog/category_detail.html'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Product.objects.filter(category=category).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'catalogs'
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        return context


class Contacts(View):
    def get(self, request, *args, **kwargs):
        context = {
            'current_page': 'contacts',
        }
        return render(request, 'catalog/contacts.html', context)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:catalogs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'catalogs'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'home'
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:catalogs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'catalogs'
        return context

    def get_success_url(self):
        return reverse('catalog:category_products', args=[self.kwargs.get("pk")])


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'home'
        return context

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get("pk")])


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('catalog:catalogs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'catalogs'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'home'
        return context


class Blog(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/post_list.html')