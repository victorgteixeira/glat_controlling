from django.contrib import admin
from .models import Produto


# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ean', 'descricao', 'quantidade', 'un_medida', 'fornecedor', 'preco', 'data_criacao', 'data_atualizacao')
    search_fields = ('nome', 'ean')
    list_filter = ('nome',)

admin.site.register(Produto, ProdutoAdmin)