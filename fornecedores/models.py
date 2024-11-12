import random
import string
from django.db import models
from cnpj_field.models import CNPJField
from django.core.validators import RegexValidator

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200, unique=False, blank=False)
    cnpj = CNPJField(max_length=15, unique=True)
    endereco = models.TextField()
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')]
    )
    email = models.EmailField()
    codigo = models.CharField(max_length=10, unique=True, blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def gerar_codigo(self):
        """Gera um código aleatório de 10 caracteres, composto por letras e números"""
        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return codigo

    def save(self, *args, **kwargs):
        """Override do método save para gerar o código antes de salvar o fornecedor"""
        if not self.codigo:
            self.codigo = self.gerar_codigo()
        super().save(*args, **kwargs)
