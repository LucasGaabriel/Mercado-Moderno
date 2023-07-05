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