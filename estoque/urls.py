from django.urls import path
from . import views

urlpatterns = [
    path('estoque_produto/', views.estoque_produto, name='estoque_produto'),
]
