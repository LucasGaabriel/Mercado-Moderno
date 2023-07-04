from django.urls import path

from . import views

app_name = "mercado_moderno"

urlpatterns = [
    path("", views.index, name="index"),
    
    path("api/cadastro/", views.cadastrar_usuario, name="cadastro"),
    path("api/login/", views.logar_usuario, name="login"),
    path("api/logout/", views.deslogar_usuario, name="logout"),
    path("api/alterar_senha/", views.alterar_senha, name='alterar_senha'),
]