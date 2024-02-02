from django.contrib import admin

from contactos.models import Categoria, Contacto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contacto)