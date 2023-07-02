from django.urls import path

from . import views

app_name = "mercado_moderno"

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.cadastrar_usuario, name="cadastro"),
    path("login/", views.logar_usuario, name="login"),
    path("logout/", views.deslogar_usuario, name="logout"),
    path("alterar_senha/", views.alterar_senha, name='alterar_senha'),
    path("home/", views.home, name="home"),
    path("produtos/", views.ProdutosView.as_view(), name="produtos"),

    # REST API
    path("api/produto-list/", views.produtoList, name="produto-list"),
    path("api/produto-detail/<str:pk>/", views.produtoDetail, name="produto-detail"),
    path("api/produto-create/", views.produtoCreate, name="produto-create"),
    path("api/produto-update/<str:pk>/", views.produtoUpdate, name="produto-update"),
    path("api/produto-delete/<str:pk>/", views.produtoDelete, name="produto-delete"),
]