from django.shortcuts import render
from lista_compras.models import Artigo


# Create your views here.
def home(request):

    # obter dados do Modelo
    artigos = Artigo.objects.all()
    
    return render(request, 'lista_compras/home.html')