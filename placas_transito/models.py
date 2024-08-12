from django.db import models
from utils.rands import new_slugify
from django.urls import reverse
from utils.images import resize_image
from django.contrib.auth.models import User
from django.utils import timezone
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


class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by('-pk')

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    objects = PostManager()

    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, default="", null=False, blank=True, max_length=255)

    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False, help_text=('Este campo precisará estar marcado para o post ser exibido publicamente.'))

    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m', blank=True, default='')

    cover_in_post_content = models.BooleanField(default=True, help_text='Se marcado, exibirá a capa dentro do post.')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_updated_by')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('placas_transito:index')
        return reverse('placas_transito:post', args=(self.slug, ))
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.title)
        current_favicon_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        super().save(*args, **kwargs)
        favicon_changed = False
        if self.cover:
            favicon_changed = current_favicon_name != self.cover.name
        if favicon_changed:
            resize_image(self.cover, 290)
        return super_save
