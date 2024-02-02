from django.urls import path
from . import views

app_name = 'lista_compras'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('adicionar/', views.add, name= 'add'),
    path('eliminar/<int:id>', views.delete, name = 'delete'),
]