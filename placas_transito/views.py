from django.shortcuts import render


def index(request):
    return render(request, 'placas_transito/pages/index.html')


def page(request):
    return render(request, 'placas_transito/pages/page.html')


def post(request):
    return render(request, 'placas_transito/pages/post.html')

