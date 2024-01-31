from django.db import models

# Create your models here.
class Artigo(models.Model):

    OPCOES = [
        ('U', 'Urgente'),
        ('N', 'Não Urgente')
    ]

    nome = models.CharField(max_length = 252)
    quantidade = models.CharField(max_length = 20, default = '1')
    urgente = models.CharField(max_length = 1, choices = OPCOES, default = 'N')

    def __str__(self) -> str:
        return self.nome + " - " + self.quantidade