from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'endereco', 'telefone', 'email', 'ativo']
        widgets = {
            'endereco': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
