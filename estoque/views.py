from django.shortcuts import render
from .models import Estoque
from produtos.models import Produto

def estoque_produto(request):
    # Obtém todos os estoques para exibir
    estoques = Estoque.objects.all()
    produtos = Produto.objects.all()
    
    # Cria um dicionário para mapear os produtos aos seus respectivos estoques
    estoque_data = {}
    for produto in produtos:
        estoque_data[produto] = Estoque.objects.filter(produto=produto)
    
    return render(request, 'estoque/estoque_produto.html', {'estoques': estoque_data})
