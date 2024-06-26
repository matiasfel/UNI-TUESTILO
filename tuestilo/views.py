from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import CustomUserCreationForm
import json


# Create your views here.

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

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