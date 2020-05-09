from django.contrib import admin
from django import forms


from .forms import (
    CategoryForm,
    ProductForm,
)

from .models import (
    Category,
    Product,
)

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    fields = ('name_category',)

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    fields = (
        'name_product', 'description', 'price', 'category', 'state', 'image',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
