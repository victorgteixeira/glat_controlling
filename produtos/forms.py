from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'ean', 'descricao', 'un_medida', 'fornecedor', 'preco', 'foto', 'codigo', 'ativo']
