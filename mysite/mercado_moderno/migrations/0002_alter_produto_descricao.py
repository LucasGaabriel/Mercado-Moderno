# Generated by Django 4.2.2 on 2023-07-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado_moderno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]