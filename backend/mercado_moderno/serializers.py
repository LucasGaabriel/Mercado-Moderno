from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ProdutoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Produto.

    Campos:
        imagem: Uma imagem do produto.
        __all__: Todos os campos referentes ao Produto
    """
    imagem = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Produto
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo do Usuario.

    Campos:
        id: O identificador único do usuário.
        username: O nome de usuário do usuário.
        password: A senha do usuário.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo ItemCarrinho.

    Campos:
        produto: O produto associado ao item do carrinho.
        quantidade: A quantidade do produto no carrinho.
    """
    class Meta:
        model = ItemCarrinho
        fields = ('produto', 'quantidade')

class CarrinhoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Carrinho.

    Campos:
        __all__: Todos os campos associados ao carrinho.
    """
    class Meta:
        model = Carrinho
        fields = '__all__'

