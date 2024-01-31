from django.urls import path
from . import views

app_name = 'lista_compras'

urlpatterns = [
    path('', views.home, name = 'home'),
]