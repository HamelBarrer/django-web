from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=250)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.name = self.name.capitalize()
        super().save(**kwargs)
