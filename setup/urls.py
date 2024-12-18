from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('produtos/', include('produtos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('clientes/', include('clientes.urls')),
    path('estoque/', include('estoque.urls')),
    path('compras/', include('compras.urls')),
    path('transferencias/', include('transferencias.urls')),
    path('vendas/', include('vendas.urls')),
    path('baixas/', include('baixas.urls')),
    path("producao/", include("producao.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
