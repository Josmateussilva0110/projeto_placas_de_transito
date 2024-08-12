from django.shortcuts import render
from django.core.paginator import Paginator
from placas_transito.models import Post

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


def page(request, slug):
    context = dict()
    return render(request, 'placas_transito/pages/page.html')


def post(request, slug):
    context = dict()
    post = Post.objects.get_published().filter(slug=slug).first()
    context['post'] = post
    return render(request, 'placas_transito/pages/post.html', context)
