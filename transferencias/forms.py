from django import forms
from .models import Transferencia
from estoque.models import Estoque

class TransferenciaForm(forms.ModelForm):
    class Meta:
        model = Transferencia
        fields = ['estoque', 'quantidade', 'tipo_transferencia']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filtro dos estoques baseado no tipo de transferência selecionado
        tipo_transferencia = self.data.get('tipo_transferencia')  # Acessa o POST para obter o tipo de transferência
        if tipo_transferencia:
            if tipo_transferencia == 'revenda_para_avarias':
                self.fields['estoque'].queryset = Estoque.objects.filter(tipo='revenda')
            elif tipo_transferencia == 'avarias_para_revenda':
                self.fields['estoque'].queryset = Estoque.objects.filter(tipo='avarias')
        else:
            # Caso ainda não tenha sido selecionado um tipo de transferência, mostrar todos os estoques
            self.fields['estoque'].queryset = Estoque.objects.all()

