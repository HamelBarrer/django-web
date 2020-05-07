from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name_category


class Product(models.Model):
    name_product = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
