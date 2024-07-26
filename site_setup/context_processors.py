from site_setup.models import SiteSetup


def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first() #pega todos os atributos da class, exibe no html
    return {'site_setup': setup}
