from django.db import models

# Create your models here.

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    n_paginas = models.IntegerField()

    def __str__(self) -> str:
        return self.nome