from django.contrib import admin
from .models import Estoque

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data_atualizacao')
    search_fields = ('produto__nome', 'tipo')
