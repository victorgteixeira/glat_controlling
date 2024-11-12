from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, HistoricoProduto
from .forms import ProdutoForm
from django.http import JsonResponse
from fornecedores.models import Fornecedor
from django.dispatch import receiver
from django.db.models.signals import pre_save


def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar_produto.html', {'form': form})


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')  # Redireciona para a lista de produtos
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto})


def buscar_fornecedores(request):
    query = request.GET.get('q', '')
    fornecedores = Fornecedor.objects.filter(nome__icontains=query)  # Filtra fornecedores pelo nome
    fornecedores_list = list(fornecedores.values('id', 'nome'))  # Retorna id e nome

    return JsonResponse(fornecedores_list, safe=False)  # Retorna como JSON


def historico_modificacoes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    historico = [
        {'data': '2024-11-01', 'campo': 'Nome', 'valor_antigo': 'Produto A', 'valor_novo': 'Produto B'},
        {'data': '2024-11-05', 'campo': 'Preço', 'valor_antigo': '10.00', 'valor_novo': '12.00'},
        {'data': '2024-11-08', 'campo': 'Quantidade', 'valor_antigo': '50', 'valor_novo': '45'}
    ]
    
    return render(request, 'produtos/historico_modificacoes_produto.html', {
        'produto': produto,
        'historico': historico
    })


@receiver(pre_save, sender=Produto)
def registrar_modificacao(sender, instance, **kwargs):
    try:
        produto_antigo = Produto.objects.get(id=instance.id)
    except Produto.DoesNotExist:
        produto_antigo = None
    
    if produto_antigo:
        if produto_antigo.nome != instance.nome:
            HistoricoProduto.objects.create(
                produto=instance,
                campo='Nome',
                valor_antigo=produto_antigo.nome,
                valor_novo=instance.nome
            )
