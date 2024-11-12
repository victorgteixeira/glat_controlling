from django.db import models
import random
import string
from django.core.exceptions import ValidationError
from cpf_field.models import CPFField

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = CPFField('cpf')
    nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nome
        
    def gerar_codigo(self):
        """Gera um código aleatório de 10 caracteres, composto por letras e números"""
        while True:
            codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if not Cliente.objects.filter(codigo=codigo).exists():
                break
        return codigo

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = self.gerar_codigo()

        super().save(*args, **kwargs)
