# Generated by Django 5.1.3 on 2024-11-12 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0010_historicoproduto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='quantidade',
        ),
    ]
