from django.db import models
from produtos.models import Produto

class Estoque(models.Model):
    TIPOS_ESTOQUE = [
        ('revenda', 'Revenda'),
        ('avarias', 'Avarias'),
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPOS_ESTOQUE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.produto.nome} - {self.tipo} - {self.quantidade} unidades'

    def adicionar_estoque(self, quantidade):
        """Método para adicionar quantidade ao estoque"""
        self.quantidade += quantidade
        self.save()

    def remover_estoque(self, quantidade):
        """Método para remover quantidade do estoque"""
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
            self.save()
        else:
            raise ValueError("Quantidade insuficiente no estoque")