from django.urls import path

from . import views

app_name = "mercado_moderno"

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.cadastrar_usuario, name="cadastro"),
    path("login/", views.logar_usuario, name="login"),
    path("deslogar_usuario/", views.deslogar_usuario, name="deslogar"),
    path("home/", views.home, name="home"),
    path("produtos/", views.produtos, name="produtos"),
    path("carrinho/", views.carrinho, name="carrinho"),
]