from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Baixa
from .forms import BaixaForm
from django.core.exceptions import ValidationError


def registrar_baixa(request):
    if request.method == "POST":
        form = BaixaForm(request.POST)
        if form.is_valid():
            baixa = form.save(commit=False)
            try:
                baixa.processar_baixa()
                baixa.save()
                messages.success(request, "Baixa registrada com sucesso e estoque atualizado!")
                return redirect('listar_baixas')
            except ValidationError as e:
                form.add_error(None, e.message)
    else:
        form = BaixaForm()
    return render(request, 'baixas/registrar_baixa.html', {'form': form})

def listar_baixas(request):
    baixas = Baixa.objects.all()
    return render(request, 'baixas/listar_baixas.html', {'baixas': baixas})
