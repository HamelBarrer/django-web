from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=14, blank=True)
    image = models.ImageField(upload_to='profile/', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
