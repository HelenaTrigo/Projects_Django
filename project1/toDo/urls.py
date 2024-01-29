from django.urls import path
from . import views

app_name = 'toDo'

urlpatterns = [
    path('', views.mostrar_tarefas, name ='home'),
    path('adicionar/', views.inserir_tarefa, name = 'inserir'),
    path('eliminar/<int:id>', views.eliminar_tarefa, name = 'eliminar'),
    path('alterar/<int:id>', views.alterar_tarefa , name = 'alterar'),
]