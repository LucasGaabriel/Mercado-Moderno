from django.contrib import admin
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin

from .models import *

# Configuração de Títulos da Página de Administração
admin.AdminSite.index_title = "Administração do Mercado Moderno"
admin.AdminSite.site_title = "Admin"

class ProdutoAdmin(admin.ModelAdmin):
    """Configuração do painel de administração para o modelo Produto"""
    list_display = ["nome", "preco", "estoque", "vendas"]
    search_fields = ["nome", "descricao"]

class ProdutoCarrinhoInline(admin.TabularInline):
    """Configuração do painel de administração para mostrar os Produtos na página de edição dos Carrinhos"""
    model = Carrinho.produtos.through
    extra = 3

class CarrinhoAdmin(admin.ModelAdmin):
    """Configuração do painel de administração para o modelo Carrinho"""
    list_display = ["usuario", "quantidade_produtos", "valor_total"]
    inlines = [ProdutoCarrinhoInline]

class ProdutoCompraInline(admin.TabularInline):
    """Configuração do painel de administração para mostrar os Produtos na página de edição dos Carrinhos"""
    model = Compra.produtos.through
    extra = 3

class CompraAdmin(admin.ModelAdmin):
    """Configuração do painel de administração para o modelo Carrinho"""
    list_display = ["usuario", "data", "quantidade_produtos", "valor"]
    inlines = [ProdutoCompraInline]

      
class UsuarioAdmin(EmailUserAdmin):
    """Configuração do painel de administração para o modelo Usuario"""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'data_nascimento')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_verified')}),
    )
        
# Desregistrar o modelo User Padrão do Django e registrar o modelo de Usuario Personalizado
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UsuarioAdmin)

# Registrar os demais modelos no painel de administração
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(Compra, CompraAdmin)

# admin.site.register(Categoria)
