# Generated by Django 5.1.3 on 2024-11-17 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0012_historicoproduto_usuario_and_more'),
        ('vendas', '0002_venda_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='codigo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='codigo_venda', to='produtos.produto'),
        ),
    ]
