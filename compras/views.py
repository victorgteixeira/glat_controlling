from django.shortcuts import render, redirect
from .models import Compra
from .forms import CompraForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def registrar_compra(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            compra.atualizar_estoque()
            messages.success(request, "Compra registrada com sucesso e estoque atualizado!")
            return redirect('listar_compras')
    else:
        form = CompraForm()

    return render(request, 'compras/registrar_compra.html', {'form': form})

def listar_compras(request):
    query = request.GET.get('q', '')
    if query:
        compras = Compra.objects.filter(
            Q(produto__nome__icontains=query) |
            Q(quantidade_comprada__icontains=query) |
            Q(data_compra__icontains=query)
        )
    else:
        compras = Compra.objects.all()

    paginator = Paginator(compras, 10)
    page_number = request.GET.get('page')
    compras_paginadas = paginator.get_page(page_number)

    return render(request, 'compras/listar_compras.html', {'compras': compras_paginadas, 'query': query})
