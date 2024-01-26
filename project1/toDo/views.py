from django.shortcuts import render

# Create your views here.
def mostrar_tarefas(request):
    return render(request, 'toDo\home.html')