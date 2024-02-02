from django.shortcuts import render
from contactos.models import Contacto

# Create your views here.

def home(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/home.html', {'contactos':contactos})
