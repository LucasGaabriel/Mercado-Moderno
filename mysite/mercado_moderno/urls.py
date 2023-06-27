from django.urls import path

from . import views

app_name = "mercado_moderno"

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.cadastrar_usuario, name="cadastro"),
    path("login/", views.logar_usuario, name="login"),
    path("deslogar/", views.deslogar_usuario, name="deslogar"),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path("home/", views.home, name="home"),
    path("produtos/", views.produtos, name="produtos"),
    path("carrinho/", views.carrinho, name="carrinho"),
]