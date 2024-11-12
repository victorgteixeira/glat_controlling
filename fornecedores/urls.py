from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fornecedores, name='lista_fornecedores'),
    path('adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('editar/<int:pk>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('excluir/<int:fornecedor_id>/', views.excluir_fornecedor, name='excluir_fornecedor'),
    path('fornecedor/<int:fornecedor_id>/itens/', views.consultar_itens_fornecedor, name='consultar_itens_fornecedor'),
]


