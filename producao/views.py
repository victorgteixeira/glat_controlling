from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producao, Ingrediente
from estoque.models import Estoque
from produtos.models import Produto

def produzir_produto(request):
    if request.method == "POST":
        produto_final_id = request.POST.get('produto_final')
        quantidade_produto = int(request.POST.get('quantidade'))
        
        produto_final = Produto.objects.get(id=produto_final_id)
        ingredientes = Ingrediente.objects.filter(produto_final=produto_final)
        
        for ingrediente in ingredientes:
            estoque_ingrediente = Estoque.objects.filter(produto=ingrediente.ingrediente, tipo='revenda').first()

            if not estoque_ingrediente:
                messages.error(request, f"Estoque não encontrado para o ingrediente: {ingrediente.ingrediente.nome}.")
                return redirect('produzir_produto')

            quantidade_necessaria = ingrediente.quantidade_necessaria * quantidade_produto

            # Verifica a disponibilidade no estoque
            if estoque_ingrediente.quantidade < quantidade_necessaria:
                messages.error(request, f"Estoque insuficiente para o ingrediente: {ingrediente.ingrediente.nome}.")
                return redirect('produzir_produto')

            # Subtrai a quantidade do estoque
            estoque_ingrediente.remover_estoque(quantidade_necessaria)

        # Adiciona o produto final ao estoque
        estoque_produto_final, created = Estoque.objects.get_or_create(produto=produto_final, tipo='revenda')
        estoque_produto_final.adicionar_estoque(quantidade_produto)

        # Registra a produção
        producao = Producao.objects.create(
            produto_final=produto_final,
            quantidade=quantidade_produto,
            sucesso=True,
            mensagem=f"Produção de {quantidade_produto} unidades de {produto_final.nome} concluída com sucesso."
        )
        producao.save()

        messages.success(request, producao.mensagem)
        return redirect('listar_producoes')

    else:
        produtos = Produto.objects.all()
        return render(request, 'producao/produzir_produto.html', {'produtos': produtos})


def cadastrar_ingredientes(request):
    if request.method == "POST":
        produto_final_id = request.POST.get("produto_final")
        ingrediente_id = request.POST.get("ingrediente")
        quantidade_necessaria = request.POST.get("quantidade_necessaria")

        produto_final = Produto.objects.get(id=produto_final_id)
        ingrediente = Produto.objects.get(id=ingrediente_id)

        Ingrediente.objects.create(
            produto_final=produto_final,
            ingrediente=ingrediente,
            quantidade_necessaria=quantidade_necessaria
        )

        messages.success(request, f"Ingrediente {ingrediente.nome} adicionado à receita de {produto_final.nome}.")
        return redirect("cadastrar_ingredientes")

    produtos = Produto.objects.all()
    return render(request, "producao/cadastrar_ingredientes.html", {"produtos": produtos})


def listar_produtos_e_ingredientes(request):
    produtos_com_ingredientes = Produto.objects.prefetch_related("ingredientes").all()
    
    return render(request, "producao/listar_produtos_e_ingredientes.html", {
        "produtos_com_ingredientes": produtos_com_ingredientes
    })


def remover_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    ingrediente.delete()
    messages.success(request, f"O ingrediente {ingrediente.ingrediente.nome} foi removido com sucesso.")
    return redirect("listar_produtos_e_ingredientes")


def listar_producoes(request):
    producoes = Producao.objects.all().order_by('-data') 
    return render(request, 'producao/listar_producoes.html', {'producoes': producoes})


def detalhar_producao(request, producao_id):
    producao = Producao.objects.get(id=producao_id)
    return render(request, 'producao/detalhar_producao.html', {'producao': producao})
