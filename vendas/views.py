from django.shortcuts import render, redirect
from .models import Venda
from .forms import VendaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.http import JsonResponse
from .models import Produto

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
    query = request.GET.get('q', '')
    data_inicial = request.GET.get('data_inicial', '')
    data_final = request.GET.get('data_final', '')
    ultimos_alterados_vendas = Venda.objects.order_by('-data_venda')[:3]

    vendas = Venda.objects.all()

    if query:
        vendas = vendas.filter(Q(produto__nome__icontains=query))

    if data_inicial:
        data_inicial = parse_date(data_inicial)
        if data_inicial:
            vendas = vendas.filter(data_venda__date__gte=data_inicial)
    if data_final:
        data_final = parse_date(data_final)
        if data_final:
            vendas = vendas.filter(data_venda__date__lte=data_final)

    paginator = Paginator(vendas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'vendas': page_obj,
        'query': query,
        'data_inicial': data_inicial,
        'data_final': data_final,
        'ultimos_alterados_vendas': ultimos_alterados_vendas,
    }

    return render(request, 'vendas/listar_vendas.html', context)
