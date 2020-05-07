from django.shortcuts import render, redirect
from django.views.generic import View

from .models import (
    Product,
)


from .forms import (
    ProductForm,
)


class ProductView(View):
    template_name = 'products/product.html'
    model = Product
    form_class = ProductForm

