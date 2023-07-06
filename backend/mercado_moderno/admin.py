from django.contrib import admin
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin

from .models import *

admin.AdminSite.index_title = "Administração do Mercado Moderno"
admin.AdminSite.site_title = "Admin"

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["nome", "preco", "estoque", "vendas"]
    search_fields = ["nome", "descricao"]

class ProdutoInline(admin.TabularInline):
    model = Carrinho.produtos.through
    extra = 3

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ["usuario", "quantidade_produtos"]
    inlines = [ProdutoInline]
    
class ItemCarrinhoInline(admin.StackedInline):
      model = ItemCarrinho
      
class UsuarioAdmin(EmailUserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Informações Pessoais', {'fields': ('first_name', 'last_name', 'data_nascimento')}),
		('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_verified')}),
	)
        

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UsuarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(Compra)
