from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View, generic
from django.views.generic import TemplateView
from authemail.views import Signup
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status, permissions, viewsets
from authemail import wrapper
from django import forms
from django.forms.forms import NON_FIELD_ERRORS
from .serializers import *
from .models import *

def index(request):
    return render(request, "mercado_moderno/index.html")

class ProdutosView(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()

class CarrinhoView(viewsets.ModelViewSet):
    serializer_class = CarrinhoSerializer
    queryset = Carrinho.objects.all()