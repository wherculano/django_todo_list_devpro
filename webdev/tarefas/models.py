from django.db import models


class Tarefa(models.Model):
    nome = models.CharField(max_length=128)
    concluida = models.BooleanField(default=False)
