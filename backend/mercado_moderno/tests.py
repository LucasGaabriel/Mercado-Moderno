from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
import json

from .models import *

class AccountsTestCase(APITestCase):
    """Classe de testes relaciona a criação de contas, usuários e autenticação."""
    register_url = "/api/accounts/signup/"
    login_url = "/api/accounts/login/"
    user_url = "/api/accounts/users/me/"
    logout_url = "/api/accounts/logout/"

    def test_register(self):
        """"Testa se registro está funcionando"""
        data = {
            "email": "user@example-email.com",
            "password": "verysecret",
            "first_name": "João",
            "last_name": "Cézar"
        }

        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """Testa se login está funcionando"""
        data = {
            "email": "user@example-email.com",
            "password": "verysecret",
            "first_name": "João",
            "last_name": "Cézar"
        }

        self.client.post(self.register_url, data)
        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token(self):
        """Testa se token recebido do login está funcionando e retornando usuário correto"""
        data = {
            "email": "user@example-email.com",
            "password": "verysecret",
            "first_name": "João",
            "last_name": "Cézar"
        }

        self.client.post(self.register_url, data)

        response = self.client.post(self.login_url, data)
        token = json.loads(response.content)['token']

        headers = {
        'Authorization': f'Token {token}'
        }

        response = self.client.get(self.user_url, headers=headers, follow=True)
        user = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(user["email"], "user@example-email.com")
        self.assertEqual(user["first_name"], "João")
        self.assertEqual(user["last_name"], "Cézar")

    def test_logout(self):
        """Testa se logout está funcionando corretamente"""
        data = {
            "email": "user@example-email.com",
            "password": "verysecret",
            "first_name": "João",
            "last_name": "Cézar"
        }

        self.client.post(self.register_url, data)

        response = self.client.post(self.login_url, data)
        token = json.loads(response.content)['token']

        headers = {
        'Authorization': f'Token {token}'
        }

        response = self.client.get(self.logout_url, headers=headers, follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


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

        c = Carrinho.objects.get(usuario=user)

        ItemCarrinho.objects.create(carrinho=c, produto=p1, quantidade=3)
        ItemCarrinho.objects.create(carrinho=c, produto=p2, quantidade=2)

        # Produto 1 = $10, Quantidade = 3 => Total=$30
        # Produto 2 = $20, Quantidade = 2 => Total=$40
        # => Total=$70

        self.assertEqual(70, c.valor_total())