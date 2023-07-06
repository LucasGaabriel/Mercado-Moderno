from django.contrib import admin
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin

from .models import *

admin.AdminSite.index_title = "Administração do Mercado Moderno"
admin.AdminSite.site_title = "Admin"

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["nome", "preco", "estoque"]
    search_fields = ["nome", "descricao"]

class UsuarioAdmin(EmailUserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal Info', {'fields': ('first_name', 'last_name')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 
									   'is_superuser', 'is_verified', 
									   'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
		('Custom info', {'fields': ('data_nascimento',)}),
	)
        
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UsuarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Carrinho)
admin.site.register(Compra)
admin.site.register(ItemCarrinho)
