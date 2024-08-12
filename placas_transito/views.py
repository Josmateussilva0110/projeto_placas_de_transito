from django.shortcuts import render
from django.core.paginator import Paginator
from placas_transito.models import Post, Page
from django.db.models import Q

PER_PAGE = 9


def index(request):
    context = dict()
    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'placas_transito/pages/index.html', context)


def category(request, slug):
    context = dict()
    posts = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'placas_transito/pages/index.html', context)


def search(request):
    context = dict()
    search_value = request.GET.get('search', '').strip()
    posts = Post.objects.get_published().filter(Q(title__icontains=search_value) | Q(excerpt__icontains=search_value) | Q(content__icontains=search_value))[:PER_PAGE]

    context['page_obj'] = posts
    context['search_value'] = search_value
    return render(request, 'placas_transito/pages/index.html', context)


def page(request, slug):
    context = dict()
    page = Page.objects.filter(is_published=True).filter(slug=slug).first()
    context['page'] = page
    return render(request, 'placas_transito/pages/page.html', context)


def post(request, slug):
    context = dict()
    post = Post.objects.get_published().filter(slug=slug).first()
    context['post'] = post
    return render(request, 'placas_transito/pages/post.html', context)
