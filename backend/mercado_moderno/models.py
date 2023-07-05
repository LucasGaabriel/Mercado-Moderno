from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='', null=True, blank=True)
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
    

class Usuario(EmailAbstractUser):
    data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    objects = EmailUserManager()


class Carrinho(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(to=Produto)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


class Compra(models.Model):
    usuario = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(to=Produto)
    data = models.DateTimeField(auto_now=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
