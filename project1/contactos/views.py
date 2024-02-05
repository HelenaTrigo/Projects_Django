from django.http import HttpResponse
from django.shortcuts import redirect, render
from contactos.models import Contacto
from contactos.forms import ContactoForm

# Create your views here.

def home(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/home.html', {'contactos':contactos})


def add(request):
    formulario = ContactoForm()
    if request.method == "POST":
        # request files permite o upload de imagens
        formulario = ContactoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('contactos:home')
    return render(request,'contactos/add.html', {'formulario':formulario})

def delete(reqeust, id):
    contacto = Contacto.objects.filter(pk = id)
    contacto.delete()
    return redirect('contactos:home')

def edit(request, id):
    try:
        contacto = Contacto.objects.get(pk = id)
    except:
        return HttpResponse("Erro: o contacto não existe. Será redircionado para nova página em 5 segundos.")
        # em html redirediona para pagina no tempo definido <meta http-equiv="refresh" content="5; URL={% url 'contactos:home' %}"/>
       
    else:
        # Cria formulario com a informação antiga do contacto
        formulario = ContactoForm(instance = contacto)
        if request.method == 'POST':
            # tem que referir a instancia do formualario (registo) para não inserir um novo
            formulario = ContactoForm(request.POST, request.FILES, instance = contacto)
            formulario.save()
            return redirect('contactos:home')
        return render(request, 'contactos/edit.html', {'formulario':formulario})