from django.db import models
from produtos.models import Produto
from django.utils import timezone


class Ingrediente(models.Model):
    produto_final = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="ingredientes")
    ingrediente = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Produto usado como ingrediente
    quantidade_necessaria = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade_necessaria} de {self.ingrediente.nome} para {self.produto_final.nome}"


class Producao(models.Model):
    produto_final = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    sucesso = models.BooleanField(default=False)
    mensagem = models.TextField(blank=True, null=True)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Produção de {self.produto_final.nome} em {self.data.strftime('%Y-%m-%d %H:%M:%S')}"
