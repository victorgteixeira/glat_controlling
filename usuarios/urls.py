from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('register/', views.register, name='register'),
    path('config-usuario/', views.config_usuario, name='config_usuario'),
] 
