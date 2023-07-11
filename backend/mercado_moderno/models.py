from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

class Produto(models.Model):
    """Modelo para armazenar informações de cada produto"""
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='', null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    vendas = models.IntegerField(default=0)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        """Retorna uma representação em string do Produto."""
        return f"{self.nome}/Preco:{self.preco}/Vendas:{self.vendas}/Estoque:{self.vendas}"
    
    def possuiEstoque(self):
        """Verifica se o produto possui estoque disponível.

        Returns:
            bool: True se o estoque for maior que zero, False caso contrário.
        """
        return True if self.estoque > 0 else False


class Usuario(EmailAbstractUser):
    """Modelo personalizado para representar um usuário."""
    data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    objects = EmailUserManager()


class Carrinho(models.Model):
    """Modelo para armazenar os Carrinhos de cada Usuário/Cliente"""
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(to=Produto, through='ItemCarrinho')

    def valor_total(self):
        """Calcula o valor total do carrinho.

        Returns:
            decimal: O valor total do carrinho.
        """
        total = 0
        itens_carrinho = ItemCarrinho.objects.filter(carrinho=self)
        for item in itens_carrinho:
            total += item.produto.preco * item.quantidade
        return total
    
    def quantidade_produtos(self):
        """Calcula a quantidade total de produtos no carrinho.

        Returns:
            int: A quantidade total de produtos no carrinho.
        """
        total = 0
        items_carrinho = ItemCarrinho.objects.filter(carrinho=self)
        for item in items_carrinho:
            total += item.quantidade
        return total
    

class ItemCarrinho(models.Model):
    """Modelo para armazenar informações de quantidade de cada produto do carrinho"""
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)


class Compra(models.Model):
    """Modelo para armazenar cada compra feita por um determinado usuário"""
    usuario = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(to=Produto, through='ItemCompra')
    data = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def quantidade_produtos(self):
        """Calcula a quantidade total de produtos da Compra.

        Returns:
            int: A quantidade total de produtos da compra.
        """
        total = 0
        items_compra = ItemCompra.objects.filter(compra=self)
        for item in items_compra:
            total += item.quantidade
        return total


class ItemCompra(models.Model):
    """Modelo para armazenar informações de quantidade de cada produto da Compra"""
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)
