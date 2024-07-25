from django.contrib import admin
from .models import Category, Page
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'id', 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {"slug": ('name',), }


@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', )
    list_display = 'id', 'title', 'is_published',
    list_display_links = 'id', 'title',
    search_fields = 'id', 'title', 'slug', 'content',
    list_per_page = 10
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {"slug": ('title',), }

