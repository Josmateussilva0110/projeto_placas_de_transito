from django.shortcuts import render
from django.core.paginator import Paginator

posts = list(range(1000))


def index(request):
    context = dict()
    pagination = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = pagination.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'placas_transito/pages/index.html', context)


def page(request):
    context = dict()
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'placas_transito/pages/page.html')


def post(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'placas_transito/pages/post.html')
