from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions
from .serializers import *
from .models import *

def index(request):
    return render(request, "mercado_moderno/index.html")

@api_view(['POST'])
def cadastrar_usuario(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logar_usuario(request):
    username = request.data.get("username")
    password = request.data.get("password")
    usuario = authenticate(request, username=username, password=password)
    if usuario is not None:
        login(request, usuario)
        return Response({"message": "Usuário logado com sucesso."}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Nome de usuário ou senha incorretos."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def deslogar_usuario(request):
    logout(request)
    return Response({"message": "Usuário deslogado com sucesso."}, status=status.HTTP_200_OK)

@api_view(['POST'])
def alterar_senha(request):
    form_senha = PasswordChangeForm(request.user, request.data)
    if form_senha.is_valid():
        user = form_senha.save()
        update_session_auth_hash(request, user)
        return Response({"message": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)
    else:
        return Response(form_senha.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def produtoList(request):
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def produtoDetail(request, pk):
    produto = Produto.objects.get(id=pk)
    serializer = ProdutoSerializer(produto, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def produtoCreate(request):
    serializer = ProdutoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def produtoUpdate(request, pk):
    produto = Produto.objects.get(id=pk)
    serializer = ProdutoSerializer(instance=produto, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def produtoDelete(request, pk):
    produto = Produto.objects.get(id=pk)
    produto.delete()
    return Response("Produto deletado com sucesso!")
