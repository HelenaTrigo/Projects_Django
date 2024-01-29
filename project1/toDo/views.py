from django.shortcuts import redirect, render
from project1.toDo.models import Tarefa
from project1.toDo.forms import *

# Create your views here.
def mostrar_tarefas(request):
    tarefas= Tarefa.objects.all().filter(concluido = False).order_by('data')
    numero = len(tarefas)
    return render(request, 'toDo\home.html', {'tarefas': tarefas, 'numero': numero})

def inserir_tarefa(request):
    # criar formulário
    formulario = TarefaForm()
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        formulario.save()
        return redirect('toDo:home')
    return render(request, 'toDo7adicionar.html', {'formulario': formulario})
    

def eliminar_tarefa(request, id):
    # eliminar tarefa com id
    tarefa1 = Tarefa.objects.get(pk = id)
    tarefa1.delete()
    #redirecionar para a página home
    return redirect('todo:home')
