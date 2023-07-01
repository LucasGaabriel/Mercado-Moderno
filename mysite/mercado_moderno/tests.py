from django.test import TestCase

from .models import Produto

class ProdutoModelTests(TestCase):
    def test_verifica_estoque_disponivel(self):
        p = Produto(estoque=10)
        self.assertTrue(p.possuiEstoque())

    def test_verifica_estoque_indisponivel(self):
        p = Produto(estoque=0)
        self.assertFalse(p.possuiEstoque())
