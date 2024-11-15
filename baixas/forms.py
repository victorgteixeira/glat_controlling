from django import forms
from .models import Baixa

class BaixaForm(forms.ModelForm):
    class Meta:
        model = Baixa
        fields = ['produto', 'quantidade_perdida', 'valor_perda']
