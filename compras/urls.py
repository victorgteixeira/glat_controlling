from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_compra, name='registrar_compra'),
    path('listar/', views.listar_compras, name='listar_compras'),
]
