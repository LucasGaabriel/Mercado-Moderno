from django.urls import path

from . import views

app_name = "mercado_moderno"

urlpatterns = [
    path("", views.index, name="index"),
    
    path("api/cadastro/", views.cadastrar_usuario, name="cadastro"),
    path("api/login/", views.logar_usuario, name="login"),
    path("api/logout/", views.deslogar_usuario, name="logout"),
    path("api/alterar_senha/", views.alterar_senha, name='alterar_senha'),

    path("api/produtos/", views.produtoList, name="produto-list"),
    path("api/produto_detail/<str:pk>/", views.produtoDetail, name="produto-detail"),
    path("api/produto_create/", views.produtoCreate, name="produto-create"),
    path("api/produto_update/<str:pk>/", views.produtoUpdate, name="produto-update"),
    path("api/produto_delete/<str:pk>/", views.produtoDelete, name="produto-delete"),
]