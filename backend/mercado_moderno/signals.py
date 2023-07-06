from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario, Carrinho

# @receiver(post_save, sender=Usuario)
# def criar_carrinho(sender, instance, created, **kwargs):
#     if created:
#         c = Carrinho(usuario=instance.usuario)
#         c.save()