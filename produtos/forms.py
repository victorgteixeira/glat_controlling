from django import forms
from .models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'ean', 'descricao', 'un_medida', 'fornecedor', 'preco', 'foto', 'codigo', 'ativo']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'codigo']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Ex: Mercearia'}),
            'codigo': forms.TextInput(attrs={'placeholder': 'Código gerado automaticamente​', 'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nome'].required = True
        self.fields['codigo'].required = False