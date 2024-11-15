from django.db import models
from estoque.models import Estoque

class Transferencia(models.Model):
    TIPO_TRANSFERENCIA = [
        ('revenda_para_avarias', 'Revenda para Avarias'),
        ('avarias_para_revenda', 'Avarias para Revenda'),
    ]

    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    tipo_transferencia = models.CharField(max_length=20, choices=TIPO_TRANSFERENCIA)
    data_transferencia = models.DateTimeField(auto_now_add=True)  # Adicionando o campo de data

    def __str__(self):
        return f"Transferência de {self.quantidade} unidades de {self.estoque.produto.nome} de {self.tipo_transferencia}"

    def realizar_transferencia(self):
        """Método para realizar a transferência entre os estoques"""
        if self.tipo_transferencia == 'revenda_para_avarias':
            if self.estoque.tipo == 'revenda' and self.estoque.quantidade >= self.quantidade:
                self.estoque.quantidade -= self.quantidade
                self.estoque.save()

                estoque_avarias, created = Estoque.objects.get_or_create(
                    produto=self.estoque.produto, tipo='avarias')

                estoque_avarias.quantidade += self.quantidade
                estoque_avarias.save()

            else:
                raise ValueError("Quantidade insuficiente no estoque de origem (Revenda)")

        elif self.tipo_transferencia == 'avarias_para_revenda':
            if self.estoque.tipo == 'avarias' and self.estoque.quantidade >= self.quantidade:
                self.estoque.quantidade -= self.quantidade
                self.estoque.save()

                estoque_revenda, created = Estoque.objects.get_or_create(
                    produto=self.estoque.produto, tipo='revenda')

                estoque_revenda.quantidade += self.quantidade
                estoque_revenda.save()

            else:
                raise ValueError("Quantidade insuficiente no estoque de origem (Avarias)")
