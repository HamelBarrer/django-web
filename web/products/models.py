from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
