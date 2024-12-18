from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, HistoricoProduto, Categoria
from .forms import ProdutoForm, CategoriaForm
from django.http import JsonResponse
from fornecedores.models import Fornecedor
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    search_query = request.GET.get('search', '') 
    ultimos_alterados = Produto.objects.order_by('-data_atualizacao')[:3]
    produtos = Produto.objects.all()

    if search_query:
        produtos = produtos.filter(Q(nome__icontains=search_query))

    paginator = Paginator(produtos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'produtos': produtos,
        'search_query': search_query,
        'page_obj': page_obj,
        'ultimos_alterados': ultimos_alterados,
    }
    return render(request, 'produtos/listar_produtos.html', context)


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        
        # Manter o fornecedor atual inalterado
        fornecedor_atual = produto.fornecedor
        
        if form.is_valid():
            produto_antigo = Produto.objects.get(id=produto_id)
            produto_atualizado = form.save(commit=False)
            produto_atualizado.fornecedor = fornecedor_atual  # Garantir que o fornecedor não seja alterado
            produto_atualizado.save()
            
            for field in produto._meta.fields:
                field_name = field.name
                valor_antigo = getattr(produto_antigo, field_name)
                valor_novo = getattr(produto_atualizado, field_name)

                if valor_antigo != valor_novo:
                    HistoricoProduto.objects.create(
                        produto=produto_atualizado,
                        campo=field_name,
                        valor_antigo=str(valor_antigo),
                        valor_novo=str(valor_novo),
                        usuario=request.user
                    )

            return redirect('listar_produtos')
    
    else:
        form = ProdutoForm(instance=produto)
    
    fornecedor_atual = produto.fornecedor.nome if produto.fornecedor else ''
    
    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto, 'fornecedor_atual': fornecedor_atual})


def buscar_fornecedores(request):
    query = request.GET.get('q', '')
    fornecedores = Fornecedor.objects.filter(nome__icontains=query)
    fornecedores_list = list(fornecedores.values('id', 'nome'))

    return JsonResponse(fornecedores_list, safe=False)


def historico_modificacoes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    historico = HistoricoProduto.objects.filter(produto=produto).order_by('-data')
    print(historico)

    paginator = Paginator(historico, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'produtos/historico_modificacoes_produto.html', {
        'produto': produto,
        'page_obj': page_obj
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

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)  # Não salva imediatamente
            if not categoria.codigo:  # Gera o código manualmente
                categoria.codigo = categoria.gerar_codigo()
            categoria.save()  # Agora salva com o código gerado
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('listar_categorias')  # Redireciona para a lista de categorias
        else:
            messages.error(request, 'Erro ao cadastrar a categoria. Por favor, verifique os campos.')
    else:
        form = CategoriaForm()

    return render(request, 'produtos/cadastrar_categoria.html', {'form': form})


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'produtos/listar_categorias.html', {'categorias': categorias})


def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria alterada com sucesso!')
            return redirect('listar_categorias') 
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'produtos/editar_categoria.html', {'form': form})