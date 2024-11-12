from django.urls import path
from . import views

urlpatterns = [
    path('estoque_produto/', views.estoque_produto, name='estoque_produto'),
    path('editar_estoque/<int:produto_id>/', views.editar_estoque, name='editar_estoque'),
]
