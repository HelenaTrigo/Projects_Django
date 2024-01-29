from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length = 255)
    concluido = models.BooleanField(default = False)
    data = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.nome
    