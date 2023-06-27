from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Produto

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


def index(request):
    return render(request, "mercado_moderno/index.html")

def home(request):
    return render(request, "mercado_moderno/home.html")

def produtos(request):
    produtos = Produto.objects.all()
    context = { "produtos": produtos }
    return render(request, "mercado_moderno/produtos.html", context)

def carrinho(request):
    return HttpResponse("Você está vendo a página com o seu carrinho, contendo todos os seus produtos desejados!")
