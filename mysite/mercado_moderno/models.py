from django.db import models

class Produto(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=100)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    vendas = models.IntegerField()
    estoque = models.IntegerField()


class Categoria(models.Model):
    Nome = models.CharField(max_length=50)
    produtos = models.ManyToManyField(to=Produto)


class Carrinho(models.Model):
    produtos = models.ManyToManyField(to=Produto)


class Endereco(models.Model):
    cep = models.DecimalField(max_digits=8, decimal_places=0)
    rua = models.CharField(max_length=50)
    numero = models.DecimalField(max_digits=5, decimal_places=0)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.OneToOneField(to=Endereco)


class Compra(models.Model):
    compra = models.ForeignKey(to=Usuario)
