from django.db import models


class Restaurante(models.Model):
    nome = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    horario = models.CharField(max_length=60)
    num_funcionarios = models.IntegerField(default=0, blank=True)
    capacidade = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.content
