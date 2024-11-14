from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_baixa, name='registrar_baixa'),
    path('listar/', views.listar_baixas, name='listar_baixas'),
]
