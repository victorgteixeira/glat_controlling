from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_transferencia, name='registrar_transferencia'),
    path('listar/', views.listar_transferencias, name='listar_transferencias'),
]
