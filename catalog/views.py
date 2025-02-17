from unicodedata import category

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from catalog.forms import CategoryForm, ProductForm, ProductModeratorForm
from catalog.models import Category, Product
from catalog.services import get_product_from_cache


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_product_from_cache()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "home"
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "catalogs"
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
        context["current_page"] = "catalogs"
        return context


class CategoryProductsView(ListView):
    model = Product
    template_name = "catalog/category_detail.html"

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs["pk"])
        return Product.objects.filter(category=category).select_related("category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "catalogs"
        context["category"] = get_object_or_404(Category, pk=self.kwargs["pk"])
        return context


class Contacts(View):
    def get(self, request, *args, **kwargs):
        context = {
            "current_page": "contacts",
        }
        return render(request, "catalog/contacts.html", context)


class CategoryCreateView(CreateView, LoginRequiredMixin):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:catalogs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "catalogs"
        return context


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "home"
        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid()


class CategoryUpdateView(UpdateView, LoginRequiredMixin):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:catalogs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "catalogs"
        return context

    def get_success_url(self):
        return reverse("catalog:category_products", args=[self.kwargs.get("pk")])


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "home"
        return context

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        else:
            raise PermissionDenied


class CategoryDeleteView(DeleteView, LoginRequiredMixin):
    model = Category
    success_url = reverse_lazy("catalog:catalogs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "catalogs"
        return context


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "home"
        return context

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm(
            "product.can_delete_product"
        )


class Blog(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog/post_list.html")
