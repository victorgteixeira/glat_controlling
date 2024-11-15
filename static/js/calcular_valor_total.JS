function calcularValorTotal() {
    var quantidade = parseInt(document.getElementById('id_quantidade_comprada').value) || 0;
    var valorUnitario = parseFloat(document.getElementById('id_valor_unitario').value) || 0;
    var valorTotal = quantidade * valorUnitario;
    document.getElementById('id_valor_total').value = valorTotal.toFixed(2);
}

document.getElementById('id_quantidade_comprada').addEventListener('input', calcularValorTotal);
document.getElementById('id_valor_unitario').addEventListener('input', calcularValorTotal);
