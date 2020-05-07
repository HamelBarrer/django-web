from django.contrib import admin
from django import forms


from .forms import (
    CategoryForm,
)

from .models import (
    Category,
    Product,
)

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    fields = ('name_category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
