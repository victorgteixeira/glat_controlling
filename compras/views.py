from django.shortcuts import render, redirect
from .models import Compra
from .forms import CompraForm
from django.contrib import messages

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
    compras = Compra.objects.all()
    return render(request, 'compras/listar_compras.html', {'compras': compras})
