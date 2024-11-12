from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transferencia
from estoque.models import Estoque
from .forms import TransferenciaForm
from django.core.exceptions import ObjectDoesNotExist

def registrar_transferencia(request):
    if request.method == "POST":
        form = TransferenciaForm(request.POST)
        if form.is_valid():
            transferencia = form.save(commit=False)
            
            try:
                transferencia.realizar_transferencia()

                transferencia.save()

                messages.success(request, "Transferência realizada com sucesso!")
                return render(request, 'transferencias/listar_transferencias.html') 
            except ValueError as e:
                form.add_error('quantidade', str(e))
            except ObjectDoesNotExist:
                form.add_error(None, "Estoque não encontrado para o produto e tipo de transferência selecionado.")
    else:
        form = TransferenciaForm()

    return render(request, 'transferencias/registrar_transferencia.html', {'form': form})

def listar_transferencias(request):
    transferencias = Transferencia.objects.all()
    return render(request, 'transferencias/listar_transferencias.html', {'transferencias': transferencias})
