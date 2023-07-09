"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  include, path
from django.conf.urls.static import static
from rest_framework import routers, permissions
from mercado_moderno import views
from mysite import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Criação do router para a API do Django Rest Framework
router = routers.DefaultRouter()
router.register('produtos', views.ProdutosView)
router.register('carrinhos', views.CarrinhoView)

# Configuração da documentação gerada pelo 'drf-yasg'
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # URLs do Mercado Moderno
    path("", include("mercado_moderno.urls")),

    # URLs da documentação da API
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # URLs da API do Django Rest Framework
    path("api/", include(router.urls)),

    # URLs de Autenticação
    path("api/accounts/", include("authemail.urls")),

    # URLs referente ao Produtos dos Carrinhos
    path('api/carrinhos/<str:pk>/produtos/', views.Produtos_Carrinho),
    path('api/carrinhos/<str:pk>/produtos/add/', views.Add_Produto_Carrinho),
    path('api/carrinhos/<str:pk>/produtos/update/', views.Update_Produto_Carrinho),
    path('api/carrinhos/<str:pk>/produtos/delete/', views.Delete_Produto_Carrinho),
    
    # URLs referente as compras do Usuario
    path('api/compras/<str:pk>/save', views.Salvar_Compra),

    # URL do Painel Administrativo
    path("admin/", admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
