from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import *
from .models import *

def index(request):
    return render(request, "mercado_moderno/index.html")

class ProdutosView(viewsets.ModelViewSet):
    """View para visualização de todos os Produtos"""
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

class CarrinhoView(viewsets.ModelViewSet):
    """View para visualização de todos os Carrinhos"""
    serializer_class = CarrinhoSerializer
    queryset = Carrinho.objects.all()

def Produtos_Carrinho(request, pk):
    """View para retornar um JSON com todos os produtos de um carrinho de um usuário com id=pk"""
    itens_carrinho = ItemCarrinho.objects.filter(carrinho__usuario__id=pk)
    serializer = ItemCarrinhoSerializer(itens_carrinho, many=True)
    JSON_data = serializer.data
    return JsonResponse(JSON_data, safe=False)
