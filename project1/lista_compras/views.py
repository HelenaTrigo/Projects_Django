from django.http import HttpResponse
from django.shortcuts import redirect, render
from lista_compras.models import Artigo
from lista_compras.forms import ArtigoForm


# Create your views here.
def home(request):

    # obter dados do Modelo
    artigos = Artigo.objects.all()
    
    return render(request, 'lista_compras/home.html', {'artigos':artigos})

def add(request):
    formulario = ArtigoForm()
    if request.method == "POST":
        formulario = ArtigoForm(request.POST)
        formulario.save()
        return redirect('lista_compras:home')
    return render(request, 'lista_compras/add.html', {'formulario':formulario})


def delete(request, id):
    try:
        artigo1 = Artigo.objects.get(pk == id)
        artigo1.delete()
    except:
        return HttpResponse("<p>Ocorreu um erro. Artigo não encontrado.<\p>")
    else:
        return redirect('lista_compras:home')