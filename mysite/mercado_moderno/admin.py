from django.contrib import admin

from .models import *

admin.AdminSite.index_title = "Administração do Mercado Moderno"
admin.AdminSite.site_title = "Admin"

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["nome", "preco", "estoque"]
    search_fields = ["nome", "descricao"]

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Carrinho)
admin.site.register(Compra)
