from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Produto

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