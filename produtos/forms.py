from django import forms
from .models import Produto
from fornecedores.models import Fornecedor


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'ean', 'descricao', 'quantidade', 'un_medida', 'fornecedor', 'preco', 'foto', 'ativo']
