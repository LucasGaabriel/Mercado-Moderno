from django.contrib import admin

from .models import *

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Carrinho)
admin.site.register(Compra)
