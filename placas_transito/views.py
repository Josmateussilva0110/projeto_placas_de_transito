from django.shortcuts import render


def index(request):
    return render(request, 'placas_transito/index.html')
