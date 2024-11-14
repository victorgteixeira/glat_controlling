from django.shortcuts import render, redirect
from .models import Venda
from .forms import VendaForm
from django.contrib import messages

def registrar_venda(request):
    if request.method == "POST":
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            try:
                venda.atualizar_estoque()
                venda.save()
                messages.success(request, "Venda registrada com sucesso e estoque atualizado!")
                return redirect('listar_vendas')
            except ValueError as e:
                form.add_error(None, str(e))
    else:
        form = VendaForm()

    return render(request, 'vendas/registrar_venda.html', {'form': form})

def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/listar_vendas.html', {'vendas': vendas})
