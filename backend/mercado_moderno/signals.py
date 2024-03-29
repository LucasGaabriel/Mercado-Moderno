from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario, Carrinho

@receiver(post_save, sender=Usuario)
def Criar_Carrinho(sender, instance, created, **kwargs):
    """Quando um usuário é cadastrado, cria um carrinho automaticamente para ele"""
    if created:
        Carrinho.objects.get_or_create(usuario=instance)