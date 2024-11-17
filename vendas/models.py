from django.db import models
from produtos.models import Produto
from estoque.models import Estoque

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="vendas")
    quantidade = models.PositiveIntegerField()
    data_venda = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True, related_name='codigo_venda')

    def __str__(self):
        return f"Venda de {self.quantidade} unidades de {self.produto.nome} em {self.data_venda}"

    def atualizar_estoque(self):
        estoque_revenda = Estoque.objects.filter(produto=self.produto, tipo='revenda').first()
        if estoque_revenda and estoque_revenda.quantidade >= self.quantidade:
            estoque_revenda.quantidade -= self.quantidade
            estoque_revenda.save()
        else:
            raise ValueError("Quantidade insuficiente no estoque de revenda.")
