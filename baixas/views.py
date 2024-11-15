from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Baixa
from .forms import BaixaForm
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator


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
                form.add_error(None, f"Ocorreu um erro: {e.message}")
                messages.error(request, f"Ocorreu um erro: {e.message}")
        else:
            messages.error(request, "Existem erros no formulário. Verifique os campos.")
    else:
        form = BaixaForm()

    return render(request, 'baixas/registrar_baixa.html', {'form': form})

def listar_baixas(request):
    baixas = Baixa.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        baixas = baixas.filter(produto__nome__icontains=search_query)

    paginator = Paginator(baixas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'baixas/listar_baixas.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })
