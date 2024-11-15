from django.shortcuts import render, redirect
from .models import Venda
from .forms import VendaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

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
    
    if query:
        vendas = Venda.objects.filter(Q(produto__nome__icontains=query))
    else:
        vendas = Venda.objects.all()
    
    paginator = Paginator(vendas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'vendas/listar_vendas.html', {'vendas': page_obj, 'query': query})
