from django.contrib import admin
from .models import Fornecedor

# Register your models here.
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'endereco', 'telefone', 'email')
    search_fields = ('nome', 'cnpj')
    list_filter = ('nome',)

admin.site.register(Fornecedor, FornecedorAdmin)