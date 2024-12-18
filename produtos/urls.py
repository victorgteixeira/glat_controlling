# produtos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('buscar-fornecedores/', views.buscar_fornecedores, name='buscar_fornecedores'),
    path('historico/<int:produto_id>/', views.historico_modificacoes_produto, name='historico_modificacoes_produto'),
    path('cadastrar/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
]
