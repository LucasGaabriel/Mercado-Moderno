from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import *

class AccountsTestCase(APITestCase):
    """Classe de testes relaciona a criação de contas, usuários e autenticação."""
    register_url = "/api/accounts/signup/"
    login_url = "/api/accounts/login/"

    def test_register(self):

        data = {
            "email": "user@example-email.com",
            "password": "verysecret",
            "first_name": "João",
            "last_name": "Cézar"
        }

        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProdutoModelTests(TestCase):
    """Classe de testes para os produtos."""
    def test_verifica_estoque_disponivel(self):
        p = Produto(estoque=10)
        self.assertTrue(p.possuiEstoque())

    def test_verifica_estoque_indisponivel(self):
        p = Produto(estoque=0)
        self.assertFalse(p.possuiEstoque())


class CarrinhoModelTests(TestCase):
    """Classe de teste para ações realizadas no carrinho"""
    def test_preco_total(self):
        user = Usuario(email="teste@gmail.com"); user.save()

        p1 = Produto(preco=10); p1.save()
        p2 = Produto(preco=20); p2.save()

        c = Carrinho(usuario=user); c.save()

        ItemCarrinho.objects.create(carrinho=c, produto=p1, quantidade=3)
        ItemCarrinho.objects.create(carrinho=c, produto=p2, quantidade=2)

        # Produto 1 = $10, Quantidade = 3 => Total=$30
        # Produto 2 = $20, Quantidade = 2 => Total=$40
        # => Total=$70

        self.assertEqual(70, c.valor_total())