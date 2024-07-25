from django.urls import path
from placas_transito import views

app_name = 'placas_transito'

urlpatterns = [
    path('', views.index, name='index'),
]


