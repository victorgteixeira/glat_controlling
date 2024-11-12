from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['produto', 'quantidade_comprada', 'fornecedor']
