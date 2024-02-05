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
        formulario = ContactoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('contactos:home')
    return render(request,'contactos/add.html', {'formulario':formulario})

def delete(reqeust, id):
    contacto = Contacto.objects.filter(pk = id)
    contacto.delete()
    return redirect('contacto:home')