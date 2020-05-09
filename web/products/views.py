from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView
from django.urls import reverse_lazy

from .models import (
    Product,
)


from .forms import (
    ProductForm,
)


class ProductView(CreateView):
    template_name = 'products/product.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('products:product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_product'] = self.form_class
        return context


class ProductList(ListView):
    template_name = 'products/snippets/products.html'
    model = Product

    def get_queryset(self):
        return Product.objects.filter(state=True).order_by('-pk')
