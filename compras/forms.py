from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['produto', 'quantidade_comprada', 'fornecedor', 'valor_unitario']

    valor_total = forms.DecimalField(max_digits=10, decimal_places=2, required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean_valor_total(self):
        quantidade = self.cleaned_data.get('quantidade_comprada')
        valor_unitario = self.cleaned_data.get('valor_unitario')
        if quantidade and valor_unitario:
            return quantidade * valor_unitario
        return 0

