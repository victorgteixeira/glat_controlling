from django.db import models
from produtos.models import Produto
from estoque.models import Estoque
from fornecedores.models import Fornecedor
from django.core.exceptions import ValidationError

class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="compras")
    quantidade_comprada = models.PositiveIntegerField()
    data_compra = models.DateField(auto_now_add=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name="compras")
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra de {self.quantidade_comprada} unidades de {self.produto.nome} do fornecedor {self.fornecedor.nome} em {self.data_compra}"

    def atualizar_estoque(self):
        """Método para atualizar o estoque do produto após a compra."""
        estoque, created = Estoque.objects.get_or_create(produto=self.produto, tipo='revenda')
        estoque.adicionar_estoque(self.quantidade_comprada)

    def clean(self):
        """Validação para garantir que a quantidade comprada seja maior que zero."""
        if self.quantidade_comprada <= 0:
            raise ValidationError('A quantidade comprada deve ser maior que zero.')
        super().clean()
