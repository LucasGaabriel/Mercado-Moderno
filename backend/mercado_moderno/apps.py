from django.apps import AppConfig
from django.db.models.signals import post_save

class MercadoModernoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mercado_moderno'

    # def ready(self):
    #     from . import signals
    #     post_save.connect(signals.criar_carrinho)
