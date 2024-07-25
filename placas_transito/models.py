from django.db import models
from utils.rands import new_slugify
from django.urls import reverse
from utils.images import resize_image
from django_summernote.models import AbstractAttachment



class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        current_file_name = str(self.file.name)
        super_save = super().save(*args, **kwargs)
        super().save(*args, **kwargs)
        favicon_changed = False
        if self.file:
            favicon_changed = current_file_name != self.file.name
        if favicon_changed:
            resize_image(self.file, 900)

        return super_save



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



class Page(models.Model):
    title = models.CharField(max_length=70,)
    slug = models.SlugField(unique=True, default="", null=False, blank=True, max_length=150)
    is_published = models.BooleanField(default=False, help_text='Se marcado a pagina vai ser publica.')

    content = models.TextField()

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('placas_transito:index')
        return reverse('placas_transito:page', args=(self.slug,))
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.title)
        return super().save(*args, **kwargs)
    

    def __str__(self) -> str:
        return self.title
