from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cpf', 'nascimento', 'telefone', 'endereco']

