from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import logout

@login_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.get(user=user)
            profile.profile_picture = form.cleaned_data['profile_picture']
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "usuarios/logout.html")

@login_required
def config_usuario(request):
    user = request.user

    # Certifique-se de que o usuário tenha um perfil associado
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    if request.method == 'POST':
        # Atualizar campos do usuário
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        # Atualizar foto do perfil, se enviada
        if 'photo' in request.FILES:
            user.profile.photo = request.FILES['photo']
            user.profile.save()  # Salva o modelo Profile

        # Alterar senha, se fornecida
        if request.POST.get('password'):
            user.set_password(request.POST.get('password'))

        # Salva o modelo User
        user.save()

        return redirect('home')

    return render(request, 'usuarios/config_usuario.html', {'user': user})