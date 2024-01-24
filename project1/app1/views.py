from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Olá</h1>")

def bemvindo(request):
    return render(request, "bem-vindo.html", {'nome':'Carlos'})