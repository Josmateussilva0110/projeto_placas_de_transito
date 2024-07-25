from django.contrib import admin
from django.http import HttpRequest
from .models import Menu_Link, SiteSetup

@admin.register(Menu_Link)
class AdminMenuLink(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path',
    list_display_links = 'id', 'text',
    search_fields = 'id', 'text', 'url_or_path',


class MenuLinkInline(admin.TabularInline):
    model = Menu_Link
    extra = 1

@admin.register(SiteSetup)
class AdminSiteSetup(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInline,


    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
