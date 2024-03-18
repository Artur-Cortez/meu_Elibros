from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=120)

    preco = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    ano_edicao = models.IntegerField()

    autor = models.CharField(max_length=120)

    genero = models.CharField(max_length=120)

    cod_ISBN = models.CharField(max_length=13)

    idioma = models.CharField(max_length=120)

    num_paginas = models.IntegerField()

    editora = models.CharField(max_length=120)

    def __str__(self):
        return self.titulo