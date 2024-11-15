from django.urls import path
from . import views

urlpatterns = [
    path("produzir/", views.produzir_produto, name="produzir_produto"),
    path("cadastrar-ingredientes/", views.cadastrar_ingredientes, name="cadastrar_ingredientes"),
     path("listar-produtos-e-ingredientes/", views.listar_produtos_e_ingredientes, name="listar_produtos_e_ingredientes"),
     path("remover-ingrediente/<int:ingrediente_id>/", views.remover_ingrediente, name="remover_ingrediente"),
     path('listar/', views.listar_producoes, name='listar_producoes'),
     path('detalhes/<int:producao_id>/', views.detalhar_producao, name='detalhar_producao'),
]
