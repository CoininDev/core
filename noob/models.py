from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preço = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade de estoque')

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('Nome', max_length=100)