from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
import json

from .models import *

class AccountsTestCase(APITestCase):
    """Classe de testes relaciona a criação de contas, usuários e autenticação utilizando as APIs"""
    register_url = "/api/accounts/signup/"
    login_url = "/api/accounts/login/"
    user_url = "/api/accounts/users/me/"
    logout_url = "/api/accounts/logout/"

    def test_register(self):
        """Testa se registro está funcionando"""
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


class CarrinhoModelTests(APITestCase):
    """Classe de teste para ações realizadas no carrinho e testes das APIs do carrinho"""
    def test_preco_total(self):
        """Testa se o preço total do carrinho está sendo calculado corretamente"""
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

    def test_add_produto_carrinho(self):
        """Verifica se a API está adicionando os produtos corretamente ao carrinho"""
        user = Usuario(email="teste@gmail.com"); user.save()
        id = user.pk

        p1 = Produto(preco=10); p1.save()
        p2 = Produto(preco=20); p2.save()

        dado1 = {
            "produto_id": p1.pk,
            "quantidade": 3
        }

        dado2 = {
            "produto_id": p2.pk,
            "quantidade": 2
        }
        
        response = self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_quantidade_produtos_apos_post(self):
        """Verifica se a quantidade de itens no carrinho está sendo atualizado corretamente"""
        user = Usuario(email="teste@gmail.com"); user.save()
        id = user.pk

        p1 = Produto(preco=10); p1.save()
        p2 = Produto(preco=20); p2.save()

        dado1 = {
            "produto_id": p1.pk,
            "quantidade": 3
        }

        dado2 = {
            "produto_id": p2.pk,
            "quantidade": 2
        }
        
        response = self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        carrinho = Carrinho.objects.get(usuario=user)
        
        self.assertEqual(carrinho.quantidade_produtos(), 5)


class CompraModelTests(APITestCase):
    """Classe de teste para as compras e testes das APIs das compras"""
    def test_realizar_compra(self):
        user = Usuario(email="teste@gmail.com"); user.save()
        id = user.pk

        p1 = Produto(preco=10); p1.save()
        p2 = Produto(preco=20); p2.save()

        dado1 = {
            "produto_id": p1.pk,
            "quantidade": 5
        }

        dado2 = {
            "produto_id": p2.pk,
            "quantidade": 7
        }
        
        self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado1)
        self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado2)

        response = self.client.post(f"/api/compras/{id}/save")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        compra = Compra.objects.get(pk=1)
        self.assertEqual(compra.quantidade_produtos(), 12)

    def test_vendas_produto(self):
        """Verifica se a quantidade de vendas de um produto modifica corretamente ao ser realizada uma compra"""
        user = Usuario(email="teste@gmail.com"); user.save()
        id = user.pk
        carrinho = Carrinho.objects.get(usuario=user)

        p1 = Produto(nome="Teste1", preco=10, estoque=50); p1.save()
        p2 = Produto(nome="Teste2", preco=10, estoque=20); p2.save()

        self.assertEqual(p1.estoque, 50)
        self.assertEqual(p2.estoque, 20)

        self.assertTrue(p1.possuiEstoque)
        self.assertTrue(p2.possuiEstoque)

        dado1 = {
            "produto_id": p1.pk,
            "quantidade": 5
        }

        dado2 = {
            "produto_id": p2.pk,
            "quantidade": 7
        }
        
        self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado1, format='json')
        self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado2, format='json')
        
        response = self.client.post(f"/api/compras/{id}/save")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        p1 = Produto.objects.get(pk=1)
        p2 = Produto.objects.get(pk=2)

        self.assertEqual(p1.vendas, 5)
        self.assertEqual(p2.vendas, 7)

    def test_compra_limpa_carrinho(self):
        """Verifica se ao realizar uma compra, o carrinho está sendo limpo corretamente"""
        user = Usuario(email="teste@gmail.com"); user.save()
        id = user.pk
        carrinho = Carrinho.objects.get(usuario=user)

        p1 = Produto(nome="Teste1", preco=10, estoque=50); p1.save()
        p2 = Produto(nome="Teste2", preco=10, estoque=20); p2.save()

        self.assertEqual(p1.estoque, 50)
        self.assertEqual(p2.estoque, 20)

        self.assertTrue(p1.possuiEstoque)
        self.assertTrue(p2.possuiEstoque)

        dado1 = {
            "produto_id": p1.pk,
            "quantidade": 5
        }

        dado2 = {
            "produto_id": p2.pk,
            "quantidade": 7
        }
        
        self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado1, format='json')
        self.client.post(f"/api/carrinhos/{id}/produtos/add/", data=dado2, format='json')
        
        self.assertEqual(carrinho.quantidade_produtos(), 12)

        response = self.client.post(f"/api/compras/{id}/save")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(carrinho.quantidade_produtos(), 0)
        