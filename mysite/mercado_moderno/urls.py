from django.urls import path

from . import views

app_name = "mercado_moderno"

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.cadastrar_usuario, name="cadastro"),
    path("login/", views.logar_usuario, name="login"),
    path("logout/", views.deslogar_usuario, name="logout"),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path("home/", views.home, name="home"),
    path("produtos/", views.ProdutosView.as_view(), name="produtos"),

    path('produtos-api', views.ProdutoListAPIView.as_view(), name="produtos-api")
]