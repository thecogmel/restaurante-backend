from django.db import models


class Restaurante(models.Model):
    nome = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    horario = models.CharField(max_length=60)
    num_funcionarios = models.IntegerField(default=0, blank=True)
    capacidade = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
