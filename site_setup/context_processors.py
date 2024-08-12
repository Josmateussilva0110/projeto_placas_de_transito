from site_setup.models import SiteSetup
from placas_transito.models import Category


def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first() #pega todos os atributos da class, exibe no html
    return {'site_setup': setup}


def category_processor(request):
    categories = Category.objects.all() #pegar todas as categorias cadastradas de forma global 
    return {'categories': categories}
