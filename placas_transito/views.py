from django.shortcuts import render
from django.core.paginator import Paginator
from placas_transito.models import Post, Page
from django.db.models import Q
from django.http import Http404

PER_PAGE = 9


def index(request):
    context = dict()
    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    context['page_title'] = 'Home - '
    return render(request, 'placas_transito/pages/index.html', context)


def category(request, slug):
    context = dict()
    posts = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if len(page_obj) == 0:
        raise Http404()
    page_title = f'{page_obj[0].category.name} - '
    context['page_obj'] = page_obj
    context['page_title'] = page_title
    return render(request, 'placas_transito/pages/index.html', context)


def search(request):
    context = dict()
    search_value = request.GET.get('search', '').strip()
    posts = Post.objects.get_published().filter(Q(title__icontains=search_value) | Q(excerpt__icontains=search_value) | Q(content__icontains=search_value))[:PER_PAGE]
    page_title = f'{search_value[:20]} - '
    
    context['page_obj'] = posts
    context['search_value'] = search_value
    context['page_title'] = page_title
    return render(request, 'placas_transito/pages/index.html', context)


def page(request, slug):
    context = dict()
    page_obj = Page.objects.filter(is_published=True).filter(slug=slug).first()
    if page_obj is None:
        raise Http404()
    page_title = f'{page_obj.title} - '
    context['page'] = page_obj
    context['page_title'] = page_title
    return render(request, 'placas_transito/pages/page.html', context)


def post(request, slug):
    context = dict()
    post_obj = Post.objects.get_published().filter(slug=slug).first()
    if post_obj is None:
        raise Http404()
    page_title = f'{post_obj.title} - '
    context['post'] = post_obj
    context['page_title'] = page_title
    return render(request, 'placas_transito/pages/post.html', context)
