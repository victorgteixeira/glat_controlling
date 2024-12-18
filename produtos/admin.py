from django.contrib import admin
from .models import Produto, Categoria


# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ean', 'descricao', 'un_medida', 'fornecedor', 'preco', 'ativo', 'foto', 'codigo')
    search_fields = ('nome', 'ean')
    list_filter = ('nome',)

admin.site.register(Produto, ProdutoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo')
    search_fields = ('nome',)
    list_filter = ('nome',)

admin.site.register(Categoria, CategoriaAdmin)