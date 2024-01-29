from django.urls import path
from . import views

app_name = 'toDo'

urlpatterns = [
    path('', views.mostrar_tarefas),
    path('adicionar/', views.inserir_tarefa, name = 'inserir'),
    path('eliminar/<int:id>', views.eliminar_tarefa, name = 'eleiminar'),
]