from django.db import models
from utils.rands import new_slugify


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
