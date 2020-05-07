from django import forms

from .models import (
    Category,
    Product,
)


class CategoryForm(forms.ModelForm):

    name_category = forms.CharField(max_length=25)

    def clean_name_category(self):
        name_category = self.cleaned_data.get('name_category')
        if Category.objects.filter(name_category=name_category).exists():
            raise forms.ValidationError('La categoria ya existe')
        return name_category

    class Meta:
        model = Category
        fields = ('name_category',)
        labels = {
            'name_category': 'Nombre de la categoria',
        }
        widgets = {
            'name_category': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name_category',
                }
            )
        }


class ProductForm(forms.ModelForm):
    name_product = forms.CharField(max_length=25)

    def clean_name_product(self):
        product = self.cleaned_data.get('name_product')
        if Product.objects.filter(name_product=name_product).exists():
            raise forms.ValidationError('El nombre del producto ya existe')
        return product

    class Meta:
        model = Product
        fields = (
            'name_product', 'description', 'price', 'category', 'state', 'image'
        )
        labels = {
            'name_product': 'Nombre del Producto',
            'description': 'Descripcion',
            'price': 'Precio',
            'category': 'Categoria',
            'state': 'Estado',
            'image': 'Imagen del Producto'
        }
        widgets = {
            'name_product': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name_product',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'description',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'price',
                }
            ),
            'category': forms.SelectMultiple(),
        }
