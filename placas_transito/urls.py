from django.urls import path
from placas_transito.views import *

app_name = 'placas_transito'

urlpatterns = [
    path('', index, name='index'),
    path('page/<slug:slug>', page, name='page'),
    path('post/<slug:slug>/', post, name='post'),
    path('category/<slug:slug>/', category, name='category'),
    path('search/', search, name='search'),
]
