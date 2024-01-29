from django.shortcuts import redirect, render
from toDo.models import Tarefa
from toDo.forms import TarefaForm

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
    return render(request, 'toDo/adicionar.html', {'formulario': formulario})
    

def eliminar_tarefa(request, id):
    # eliminar tarefa com id
    tarefa1 = Tarefa.objects.get(pk = id)
    tarefa1.delete()
    #redirecionar para a página home
    return redirect('toDo:home')


def alterar_tarefa(request,id):
    #obter a informação antiga daquela tarefa
    tarefa1 = Tarefa.objects.get(pk=id)
    if request.method == 'GET':
            formulario = TarefaForm(instance=tarefa1)
            return render(request,'toDo/alterar.html', {'formulario':formulario})
    elif request.method == 'POST':
        formulario = TarefaForm(request.POST, instance=tarefa1)
        #update
        formulario.save()
        return redirect('toDo:home')
