from django.shortcuts import render, redirect, get_object_or_404
from .models import Fornecedor
from .forms import FornecedorForm
from django.contrib import messages
from produtos.models import Produto


# Lista de fornecedores
def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/lista_fornecedores.html', {'fornecedores': fornecedores})

# Adicionar fornecedor
def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedores/adicionar_fornecedor.html', {'form': form})

# Editar fornecedor
def editar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedores/editar_fornecedor.html', {'form': form})


def excluir_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)

    if request.method == 'POST':
        fornecedor.delete()
        messages.success(request, f'Fornecedor {fornecedor.nome} excluído com sucesso!')
        return redirect('lista_fornecedores') 
    else:
        return render(request, 'fornecedores/excluir_fornecedor.html', {'fornecedor': fornecedor})
    

def consultar_itens_fornecedor(request, fornecedor_id):
    # Buscar o fornecedor pelo ID
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    
    # Buscar os produtos associados a esse fornecedor
    produtos = Produto.objects.filter(fornecedor=fornecedor)

    # Passar o fornecedor e os produtos para o template
    return render(request, 'fornecedores/consultar_itens_fornecedor.html', {'fornecedor': fornecedor, 'produtos': produtos})