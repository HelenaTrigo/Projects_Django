from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length = 100, unique = True)

    def __str__(self) -> str:
        return self.categoria
    
    class Meta:
        ordering = ['categoria']

class Contacto(models.Model):
    nome = models.CharField(max_length = 225)
    telemovel = models.CharField(max_length = 20)
    email = models.EmailField(blank = True, null = True)
    telemovel2 = models.CharField(max_length = 20, blank = True, null = True)
    favorito = models.BooleanField(default = False)
    
    # py -m pip install Pillow para usar ImageField
    foto = models.ImageField(upload_to = 'contactos/fotos/', blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, blank = True, null = True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        ordering = ['nome']


