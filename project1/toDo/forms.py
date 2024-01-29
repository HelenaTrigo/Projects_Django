from django import forms
from toDo.models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta: 
        model = Tarefa
        fields = "__all__"
        #fields = ('nome',)   # se for só um campo... tem que ser ('campo1',)
        #fields = ('nome','concluido')