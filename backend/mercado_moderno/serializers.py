from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ProdutoSerializer(serializers.ModelSerializer):
    imagem = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Produto
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    
    class Meta:
        model = ItemCarrinho
        fields = ('produto', 'quantidade')

class CarrinhoSerializer(serializers.ModelSerializer):
    items = ItemCarrinhoSerializer(many=True, read_only=True)

    class Meta:
        model = Carrinho
        fields = '__all__'

