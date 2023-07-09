from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

# def index(request):
#     return render(request, "mercado_moderno/index.html")

class ProdutosView(viewsets.ModelViewSet):
    """View para visualização de todos os Produtos"""
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

class CarrinhoView(viewsets.ModelViewSet):
    """View para visualização de todos os Carrinhos"""
    serializer_class = CarrinhoSerializer
    queryset = Carrinho.objects.all()

@api_view(['GET'])
def Produtos_Carrinho(request, pk):
    """
    View para retornar um JSON com todos os produtos de um carrinho de um usuário com id=pk.

    Args:
        request: A requisição HTTP recebida.
        pk: O id do usuário.

    Returns:
        JsonResponse: Um JSON contendo os dados dos produtos no carrinho do usuário.
    """
    items_carrinho = ItemCarrinho.objects.filter(carrinho__usuario__id=pk)
    serializer = ItemCarrinhoSerializer(items_carrinho, many=True)
    JSON_data = serializer.data
    return JsonResponse(JSON_data, safe=False)


@api_view(['POST'])
def Add_Produto_Carrinho(request, pk):
    """
    View para adicionar um produto ao carrinho de um usuário com id=pk.

    Args:
        request: A requisição HTTP recebida.
        pk: O id do usuário do carrinho.

    Returns:
        Response: Uma resposta contendo os dados do item adicionado ao carrinho
    """
    carrinho = get_object_or_404(Carrinho, usuario__id=pk)

    produto_id = request.data.get('produto_id')
    quantidade = request.data.get('quantidade')

    produto = get_object_or_404(Produto, id=produto_id)

    item_carrinho, _ = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    item_carrinho.quantidade = quantidade
    item_carrinho.save()

    serializer = ItemCarrinhoSerializer(item_carrinho)
    return Response(data=serializer.data)

@api_view(['PUT'])
def Update_Produto_Carrinho(request, pk):
    """
    View para atualizar a quantidade de um produto no carrinho de um usuário com id=pk.

    Args:
        request: A requisição HTTP recebida.
        pk: O id do usuário do carrinho.

    Returns:
        Response: Uma resposta contendo os dados do item atualizado do carrinho.
    """
    carrinho = get_object_or_404(Carrinho, usuario__id=pk)

    produto_id = request.data.get('produto_id')
    quantidade = request.data.get('quantidade')

    item_carrinho = get_object_or_404(ItemCarrinho, carrinho=carrinho, produto__id=produto_id)
    item_carrinho.quantidade = quantidade
    item_carrinho.save()

    serializer = ItemCarrinhoSerializer(item_carrinho)
    return Response(data=serializer.data)

@api_view(['DELETE'])
def Delete_Produto_Carrinho(request, pk):
    """
    View para excluir um produto do carrinho de um usuário com id=pk.

    Args:
        request: A requisição HTTP recebida.
        pk: O id do usuário do carrinho.

    Returns:
        Response: Uma resposta com uma mensagem indicando que o produto foi excluído com sucesso.
    """
    carrinho = get_object_or_404(Carrinho, usuario__id=pk)

    produto_id = request.data.get('produto_id')

    item_carrinho = get_object_or_404(ItemCarrinho, carrinho=carrinho, produto__id=produto_id)
    item_carrinho.delete()

    return Response({'message': 'Produto excluído do carrinho com sucesso!'})

@api_view(['POST'])
def Salvar_Compra(request, pk):
    """
    View para salvar uma compra do usuário com id=pk.

    Args:
        request: A requisição HTTP recebida.
        pk: O id do usuário a salvar a compra.

    Returns:
        Response: Uma resposta contendo os dados salvos da compra
    """
    usuario = get_object_or_404(Usuario, id=pk)
    carrinho = get_object_or_404(Carrinho, usuario__id=pk)

    produtos_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
    compra = Compra.objects.create(usuario=usuario, valor=carrinho.valor_total())

    for item_carrinho in produtos_carrinho:
        ItemCompra.objects.create(compra=compra, produto=item_carrinho.produto, quantidade=item_carrinho.quantidade)
        
        # Acrescenta a quantidade de produtos vendidos do produto
        item_carrinho.produto.vendas += item_carrinho.quantidade
        item_carrinho.produto.save()

    compra.save()
    carrinho.produtos.clear()

    serializer = CompraSerializer(compra)
    return Response(data=serializer.data)
