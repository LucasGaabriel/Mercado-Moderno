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

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'mercado_moderno/cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect("/home")
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'mercado_moderno/login.html', {'form_login': form_login})

def deslogar_usuario(request):
    logout(request)
    return redirect('/')

@login_required
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('/home')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'mercado_moderno/alterar_senha.html', {'form_senha': form_senha})

@login_required
def home(request):
    return render(request, "mercado_moderno/home.html")

class ProdutosView(LoginRequiredMixin, generic.ListView):
    model = Produto
    template_name = 'mercado_moderno/produtos.html'
    context_object_name = "produtos"

    def get_queryset(self):
        return Produto.objects.all()

# @api_view(['GET'])
# class ProdutoListAPIView(APIView):
#     def get(self, request):
#         produtos = Produto.objects.all()
#         serializer = ProdutoSerializer(produtos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


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
