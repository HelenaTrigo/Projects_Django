from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    response = requests.get('https://catfact.ninja/fact')
    cat_info = response.json()
    return render(request, 'mostrar_api/home.html', {'dados': cat_info})