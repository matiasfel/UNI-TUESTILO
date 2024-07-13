from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth import views as auth_views

# Create your views here.

def base(request):
    context = {}
    return render(request, 'tuestilo/base.html', context)

def info(request):
    context = {}
    return render(request, 'tuestilo/info.html', context)

def catalogo(request):
    context = {}
    return render(request, 'tuestilo/catalogo.html', context)

def contacto(request):
    context = {}
    return render(request, 'tuestilo/contacto.html', context)

class CustomLoginView(auth_views.LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('base')
        return super().dispatch(request, *args, **kwargs)

def register(request):
    if request.user.is_authenticated:
        return redirect('base')  # Cambia 'base' por el nombre de la vista a la que quieras redirigir

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('base')  # Te redirige hacia la página principal con el usuario logueado
        else:
            return redirect('register')  # Te mantiene en la página de registrarse sin ningún usuario
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required

def carro(request):
    context = {}
    return render(request, 'tuestilo/carro.html', context)

# Verificar si el usuario es administrador

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)

def crud(request):
    users = User.objects.all()
    return render(request, 'tuestilo/crud.html', {'users': users})

@user_passes_test(is_admin)
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tuestilo/add_user.html', {'form': form})

@user_passes_test(is_admin)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = AdminPasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = AdminPasswordChangeForm(user)
    return render(request, 'tuestilo/edit_user.html', {'form': form})

@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('crud')
    return render(request, 'tuestilo/delete_user.html', {'user': user})
