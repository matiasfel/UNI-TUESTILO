from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

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

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('base') # Te renvia hacia la pagina principal con el usuario logeado
        else:
            return redirect('register') # Te mantiene en la pagina de registrarse sin ningun usuario.
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required

def carro(request):
    context = {}
    return render(request, 'tuestilo/carro.html', context)

def conf_usuario(request):
    context = {}
    return render(request, 'tuestilo/conf_usuario.html', context)

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required

def conf_admin(request):
    context = {}
    return render(request, 'tuestilo/conf_admin.html', context)