from django.shortcuts import render, get_object_or_404
from .models import Estoque
from produtos.models import Produto

def estoque_produto(request):
    produtos_estoques = {}
    for estoque in Estoque.objects.all():
        if estoque.produto not in produtos_estoques:
            produtos_estoques[estoque.produto] = []
        produtos_estoques[estoque.produto].append(estoque)

    return render(request, 'estoque/estoque_produto.html', {'produtos_estoques': produtos_estoques})

def editar_estoque(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    estoque = Estoque.objects.filter(produto=produto) 

    return render(request, 'estoque/editar_estoque.html', {'produto': produto, 'estoque': estoque})