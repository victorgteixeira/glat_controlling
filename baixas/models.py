from django.db import models
from produtos.models import Produto
from estoque.models import Estoque
from django.core.exceptions import ValidationError

class Baixa(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='baixas')
    quantidade_perdida = models.PositiveIntegerField()
    data_baixa = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Baixa de {self.quantidade_perdida} unidades de {self.produto.nome} por perda em {self.data_baixa}"

    def processar_baixa(self):
        """Processa a baixa no estoque de avarias."""
        try:
            estoque_avarias = Estoque.objects.get(produto=self.produto, tipo='avarias')
            if estoque_avarias.quantidade >= self.quantidade_perdida:
                estoque_avarias.quantidade -= self.quantidade_perdida
                estoque_avarias.save()
            else:
                raise ValidationError("Quantidade insuficiente no estoque de avarias para realizar a baixa.")
        except Estoque.DoesNotExist:
            raise ValidationError("Estoque de avarias não encontrado para o produto.")
