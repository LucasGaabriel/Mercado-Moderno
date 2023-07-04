from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    vendas = models.IntegerField(default=0)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
    
    def possuiEstoque(self):
        if self.estoque > 0:
            return True
        else:
            return False
    

class Categoria(models.Model):
    Nome = models.CharField(max_length=50)
    produtos = models.ManyToManyField(to=Produto)


class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=8)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.OneToOneField(to=Endereco, on_delete=models.SET_NULL, null=True)


class Carrinho(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(to=Produto)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


class Compra(models.Model):
    cliente = models.ForeignKey(to=Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(to=Produto)
    data = models.DateTimeField(auto_now=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
